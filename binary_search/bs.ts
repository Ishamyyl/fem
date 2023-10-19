
export default function binary_search<T>(arr: T[], n: T): boolean {
  let lo = 0
  let hi = arr.length
  do {
    const m = Math.floor(lo + (hi - lo) / 2) // midpoint
    const v = arr[m]

    if (v === n) return true
    if (v > n) {
      hi = m // move higher bounds down, exclusive
    } else {
      lo = m + 1 // move lower bounds up, inclusive
    }
  } while (lo < hi)
  return false
}

let n = [1, 3, 6, 89, 123, 1112, 4444, 4445, 4446, 4447, 5555, 12345, 112345]
let c = [...n, 4448, 12346, 4443, 0, 112346]
console.log(n)
for (let i of c) {
  console.log(binary_search(n, i), i)
}
