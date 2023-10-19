"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.bubble_sort_endswap = exports.bubble_sort_swap = void 0;
/**
 * Perform in-place bubble sort, swapping whenever a bigger element is found.
 * O(m*n^2)
 */
function bubble_sort_swap(arr) {
    for (var i = 0; i < arr.length; ++i) {
        for (var j = 0; j < arr.length - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                var tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}
exports.bubble_sort_swap = bubble_sort_swap;
/**
 * Perform in-place bubble sort, swapping only once the index of the biggest element is known
 * O(k*n^2) where k < m from above
 */
function bubble_sort_endswap(arr) {
    for (var i = 0; i < arr.length; ++i) {
        var biggest_index = 0;
        var end = arr.length - i - 1; // there are `i` elements in their proper place at the back
        for (var j = 0; j <= end; ++j) { // from the beginning up to and including the end
            if (arr[j] > arr[biggest_index]) { // compare the current element with the known biggest element
                biggest_index = j; // if it's bigger, mark its spot as known biggest
            }
        }
        var tmp = arr[end]; // swap the biggest with the end
        arr[end] = arr[biggest_index];
        arr[biggest_index] = tmp;
    }
}
exports.bubble_sort_endswap = bubble_sort_endswap;
var n = [3, 6, 8, 1, 3, 78, 9, 4, 32];
var m = __spreadArray([], n, true);
console.log(n);
bubble_sort_swap(n);
console.log(n);
bubble_sort_endswap(m);
console.log(m);
