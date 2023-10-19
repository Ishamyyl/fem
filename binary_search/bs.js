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
function binary_search(arr, n) {
    var lo = 0;
    var hi = arr.length;
    do {
        var m = Math.floor(lo + (hi - lo) / 2); // midpoint
        var v = arr[m];
        // console.log(lo, m, hi)
        if (v === n)
            return true;
        if (v > n) {
            hi = m; // move higher bounds down, exclusive
        }
        else {
            lo = m + 1; // move lower bounds up, inclusive
        }
        // console.log(lo, hi)
    } while (lo < hi);
    return false;
}
exports.default = binary_search;
var n = [1, 3, 6, 89, 123, 1112, 4444, 4445, 4446, 4447, 5555, 12345, 112345];
var c = __spreadArray(__spreadArray([], n, true), [4448, 12346, 4443, 0, 112346], false);
console.log(n);
for (var _i = 0, c_1 = c; _i < c_1.length; _i++) {
    var i = c_1[_i];
    console.log(binary_search(n, i), i);
}
