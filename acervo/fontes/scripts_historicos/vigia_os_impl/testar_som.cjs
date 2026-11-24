const fs=require('fs'),path=require('path');
require('./testar_pane_audio.cjs');
const root=path.resolve(__dirname,'../..');
fs.copyFileSync(path.join(root,'tmp/vigia_os_impl/pane_audio.json'),path.join(root,'tmp/vigia_os_impl/som.json'));