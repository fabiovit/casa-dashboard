const base = "/casa-dashboard-static/";
const version = "1.0.0";
const parts = 10;
const sources = await Promise.all(Array.from({length: parts}, (_, i) =>
  fetch(`${base}casa-dashboard-panel.part${i}.txt?v=${version}`, {cache: "no-store"}).then(r => {
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
