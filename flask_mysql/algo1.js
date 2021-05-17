/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };
  
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
  function zipArraysIntoMap(keys, values) {
      let new_map= new Map();
      for (var i = 0; i<keys.length;i++){
          new_map[keys[i]]=values[i]
      }
      return new_map;

  }
  console.log(zipArraysIntoMap(keys1,vals1))

// **************************************************************************************************************************************************
// **************************************************************************************************************************************************
// **************************************************************************************************************************************************

  /* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    var new_map= new Map()
    for(var key in obj){
        new_map[obj[key]]=key
    }
    return new_map
}
console.log(invertObj(obj1))

/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums1 = [-2, 5, 7, 0, 3,0];


/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
  for(i=1;i<nums.length;i++){
    var left = 0;
    var right = 0;
    for(j=0;j<i;j++){
      left+=nums[j];
    }
    for(z=i+1;z<nums.length;z++){
      right +=nums[z];
    }
    if(left == right){
      return i;
    }
  } 
  return -1
}
balanceIndex(nums1)

module.exports = { balanceIndex };

// **********************************************************************
// **********************************************************************
// **********************************************************************


/* 
  Balance Point
  Write a function that returns whether the given
  array has a balance point BETWEEN indices, 
  where one side’s sum is equal to the other’s. 
*/

const nums1 = [1, 2, 3, 4, 10];
const expected1 = true;
// Explanation: between indices 3 & 4

const nums2 = [1, 2, 4, 2, 1];
const expected2 = false;

/**
 * Determines if there is a balance point BETWEEN indexes where the sum of the
 *    left side is equal to the sum of the right side of the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {boolean} Indicates if a balance point exists.
 */
function balancePoint(nums) {
  for(i=0;i<nums.length;i++){
    var left =0
    var right =0
    for(j=0;j<i;j++){
      left += nums[j];
    }
    for(z=i;z<nums.length;z++){
      right += nums[z];
    }
    if(left == right){
      return true;
    }
  }
  return false
}

module.exports = { balancePoint };