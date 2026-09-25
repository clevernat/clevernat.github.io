// Refresh videos.json (latest public AI Walkthru uploads) for the hub's "Latest videos" section.
// Run from anywhere: node sites/clevernat.github.io/update_videos.cjs  — reads the workspace .env + youtube/yt-token.json.
const path = require('path'), fs = require('fs'); const WS = path.resolve(__dirname, '../..');
require(path.join(WS, 'node_modules/dotenv')).config({ path: path.join(WS, '.env'), quiet: true });
const { google } = require(path.join(WS, 'node_modules/googleapis'));
const o = new google.auth.OAuth2(process.env.YT_CLIENT_ID, process.env.YT_CLIENT_SECRET, 'http://localhost:5858');
o.setCredentials(JSON.parse(fs.readFileSync(path.join(WS, 'youtube/yt-token.json'), 'utf8')));
const yt = google.youtube({ version: 'v3', auth: o });
const secs = d => { const m = d.match(/PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/) || []; return (+m[1] || 0) * 3600 + (+m[2] || 0) * 60 + (+m[3] || 0); };
(async () => {
  const ch = await yt.channels.list({ part: ['contentDetails'], mine: true });
  const pl = await yt.playlistItems.list({ part: ['contentDetails'], playlistId: ch.data.items[0].contentDetails.relatedPlaylists.uploads, maxResults: 30 });
  const v = await yt.videos.list({ part: ['snippet', 'status', 'contentDetails'], id: pl.data.items.map(i => i.contentDetails.videoId) });
  const pub = v.data.items.filter(x => x.status.privacyStatus === 'public')
    .sort((a, b) => b.snippet.publishedAt.localeCompare(a.snippet.publishedAt))
    .map(x => { const s = secs(x.contentDetails.duration); return { id: x.id, title: x.snippet.title.replace(/\s*#shorts?\b/ig, '').trim(), date: x.snippet.publishedAt.slice(0, 10), short: s <= 180, len: s >= 3600 ? '' : `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}` }; });
  const out = { updated: new Date().toISOString().slice(0, 10), long: pub.filter(x => !x.short).slice(0, 4), shorts: pub.filter(x => x.short).slice(0, 6) };
  const f = path.join(__dirname, 'videos.json'); const old = fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : '';
  const next = JSON.stringify(out, null, 1);
  if (JSON.stringify({ ...JSON.parse(old || '{}'), updated: 0 }) === JSON.stringify({ ...out, updated: 0 })) { console.log('unchanged'); return; }
  fs.writeFileSync(f, next); console.log('videos.json updated', out.long.length, 'long,', out.shorts.length, 'shorts');
})().catch(e => { console.error('ERR', String(e.message).slice(0, 200)); process.exit(1); });
