export default function linear_search<T>(arr: T[], e: T): boolean {
  for (let i = 0; i < arr.length; ++i) {
    if (e === arr[i])
      return true
  }
  return false
}

export function linear_search_foreach<T>(arr: T[], e: T): boolean {
  for (let v of arr) {
    if (e === v)
      return true
  }
  return false
}
