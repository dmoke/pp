export function bouncingBall(
  h: number,
  bounce: number,
  window: number,
): number {
  if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1;
  let nextBounce: number = h * bounce;
  let windowPasses: number = 1;
  while (nextBounce > window) {
    windowPasses += 2;
    nextBounce *= bounce;
  }
  return windowPasses;
}

console.log(bouncingBall(3.0, 0.66, 1.5));
