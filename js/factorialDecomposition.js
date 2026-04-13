//https://www.codewars.com/kata/5a045fee46d843effa000070

function decomp(n) {
  let result = "";

  for (let prime of getPrimes(n)) {
    let order = countFactorInFactorial(n, prime);
    result += `${prime}${order > 1 ? "^" + order : ""} * `;
  }
  return result.substring(0, result.length - 2);
}

function countFactorInFactorial(n, p) {
  let count = 0;

  while (n > 0) {
    n = Math.floor(n / p);
    count += n;
  }

  return count;
}

function getPrimes(max) {
  const sieve = new Array(max + 1).fill(true);
  sieve[0] = sieve[1] = false;

  for (let i = 2; i <= Math.sqrt(max); i++) {
    if (sieve[i]) {
      for (let j = i * i; j <= max; j += i) {
        sieve[j] = false;
      }
    }
  }

  return sieve.reduce((primes, isPrime, num) => {
    if (isPrime) primes.push(num);
    return primes;
  }, []);
}

console.log(decomp(17)); // -> "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17"
