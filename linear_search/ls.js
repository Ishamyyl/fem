"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.linear_search_foreach = void 0;
function linear_search(arr, e) {
    for (var i = 0; i < arr.length; ++i) {
        if (e === arr[i])
            return true;
    }
    return false;
}
exports.default = linear_search;
function linear_search_foreach(arr, e) {
    for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
        var v = arr_1[_i];
        if (e === v)
            return true;
    }
    return false;
}
exports.linear_search_foreach = linear_search_foreach;
