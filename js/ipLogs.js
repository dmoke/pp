function detectBruteForce(logs) {
  return [...logs.reduce((acc, next) => {
    const [ip, msg] = next.split(" ");

    if (!acc.counts[ip]) acc.counts[ip] = 0;

    if (msg === "LOGIN_FAIL") {
      acc.counts[ip]++;
      if (acc.counts[ip] === 3) acc.result.add(ip);
    } else if (msg === "LOGIN_SUCCESS") {
      acc.counts[ip] = 0;
    }

    return acc;
  }, { counts: {}, result: new Set() }).result].sort();
}

let logs = [
  "192.168.1.1 LOGIN_FAIL user=admin",
  "192.168.1.1 LOGIN_FAIL user=admin",
  "192.168.1.1 LOGIN_FAIL user=root",
  "10.0.0.5 LOGIN_FAIL user=test",
  "10.0.0.5 LOGIN_SUCCESS user=test",
];
const result = detectBruteForce(logs); // ["192.168.1.1"]
console.log(result);
