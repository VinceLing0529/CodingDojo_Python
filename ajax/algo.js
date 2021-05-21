const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "         ";
const expected2 = "";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
/* 1.Loop through whole string and check if the current index is not space
2.if the current index is space, and current index +1 is non space, then we can also use it
3.
*/
function trim(str) {
    var new_string = ""
    for(var i = 0; i<str.length; i++){
        if(str[i]!=" "){
            new_string+=str[i]
        }
        else if(str[i+1]!=" " && str[i-1]!=" "){
            console.log(str[i])
            new_string+=str[i]
        }
    }
    return new_string
}

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const nums11 = [3, 5, 4, 3, 4, 6, 5];
const expected11 = 6;

const nums12 = [3, 5, 5];
const expected12 = 3;

const nums13 = [3, 3, 5];
const expected13 = 5;

const nums14 = [5];
const expected14 = 5;

const nums15 = [];
const expected15 = null;

const nums16 = [3, 5, 4, 3, 4, 6, 5, 7];
const expected16 = 6;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 * 1.Loop through the array for each loop
 * 2.create a dict for store the unique value
 * 3.if the current index in array is not in dict, we add it as a key and assign it with value of 1
 * 4. if it is a key already, we add the value by 1
 * 5.sort the di
 */
function firstNonRepeated(nums) {
    var dic={}
    var final=0
    for(i=0; i<nums.length;i++){
        if(!(nums[i] in dic)){
            dic[nums[i]]=1;
        }
        else{
            dic[nums[i]]+=1;
        }
    }
    for(i in dic){
        if(dic[i]==1){
            final= i
            return final 
        }
    }
}

const nums11 = [3, 5, 4, 3, 4, 6, 5];
const expected11 = 6;

const nums12 = [3, 5, 5];
const expected12 = 3;

const nums13 = [3, 3, 5];
const expected13 = 5;

const nums14 = [5];
const expected14 = 5;

const nums15 = [];
const expected15 = null;

const nums16 = [3, 5, 4, 3, 4, 6, 5, 7];
const expected16 = 6;
var obj = { a: 'test1', b: 'test2' };
if (Object.values(obj).indexOf('test1') > -1) {
   console.log('has test1');
}


function toCamelCase(str){

    for(i = 0; i<str.length; i++){
        if (str[i] == "-" || str[i] == "_"){
            
            str = str.substring(0, [i])+str.charAt(i+1).toUpperCase() +str.substring([i+2], str.length);

        }
        
    }
    return(str)
}
str1="the-stealth-warrior"

console.log(toCamelCase(str1))
