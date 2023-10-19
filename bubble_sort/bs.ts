/**
 * Perform in-place bubble sort, swapping whenever a bigger element is found.
 * O(m*n^2)
 */
export function bubble_sort_swap<T>(arr: T[]): void {
  for (let i = 0; i < arr.length; ++i) {
    for (let j = 0; j < arr.length - 1 - i; ++j) {
      if (arr[j] > arr[j + 1]) {
        const tmp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = tmp
      }
    }
  }
}

/**
 * Perform in-place bubble sort, swapping only once the index of the biggest element is known
 * O(k*n^2) where k < m from above
 */
export function bubble_sort_endswap<T>(arr: T[]): void {
  for (let i = 0; i < arr.length; ++i) {
    let biggest_index = 0
    let end = arr.length - i - 1 // there are `i` elements in their proper place at the back
    for (let j = 0; j <= end; ++j) { // from the beginning up to and including the end
      if (arr[j] > arr[biggest_index]) { // compare the current element with the known biggest element
        biggest_index = j  // if it's bigger, mark its spot as known biggest
      }
    }
    const tmp = arr[end] // swap the biggest with the end
    arr[end] = arr[biggest_index]
    arr[biggest_index] = tmp
  }
}

let n = [3, 6, 8, 1, 3, 78, 9, 4, 32];
let m = [...n];
console.log(n);
bubble_sort_swap(n);
console.log(n);
bubble_sort_endswap(m);
console.log(m);
