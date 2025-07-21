function roughEstimate(x: number): number {
  if (x < 0) x = -x;
  return Math.sqrt(x) * 1.2;
}

const samples = [0, 2, 3, 7, 12];
for (const v of samples) {
  console.log(v + " -> " + roughEstimate(v).toFixed(3));
}
