/**
 * This function takes an array of login logs as input. Each log is a string where the first part is the IP address and the second part is the message.
 * The message can be "LOGIN_FAIL" or "LOGIN_SUCCESS". The function should return an array of IP addresses that have had three failed login attempts.
 * 
 * The function uses the reduce function to accumulate the counts of login attempts per IP address. If the count is three, the IP is added to a Set data structure.
 * The reduce function is called with an initial value of an object containing an empty counts object and a new Set for the result.
 * 
 * The counts object is used to keep track of the number of login attempts per IP. It is updated by incrementing the count for each "LOGIN_FAIL" message or resetting 
 * the count for each "LOGIN_SUCCESS" message. If the count for an IP reaches three, it is added to the result Set.
 * 
 * Finally, the function returns the sorted array of IP addresses that have had three failed login attempts.
 *
 * @param {Array} logs - An array of login logs.
 * @returns {Array} - An array of IP addresses that have had three failed login attempts.
 */
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
