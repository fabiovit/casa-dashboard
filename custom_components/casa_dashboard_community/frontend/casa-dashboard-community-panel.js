const base = "/casa-dashboard-community-static/";
const version = "1.1.0";
const parts = 15;
const sources = await Promise.all(Array.from({length: parts}, (_, i) =>
  fetch(`${base}casa-dashboard-community-panel.part${i}.txt?v=${version}`, {cache: "no-store"}).then(r => {
    if (!r.ok) throw new Error(`Casa Dashboard: impossibile caricare parte ${i}`);
    return r.text();
  })
));
const blob = new Blob([sources.join("")], {type: "text/javascript"});
const url = URL.createObjectURL(blob);
try {
  await import(url);
} finally {
  URL.revokeObjectURL(url);
}
