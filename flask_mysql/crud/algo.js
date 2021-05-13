
str1 = "abcABC";
expected1 = "abcABC";

str2 = "helloo";
expected2 = "helo";


function stringDedupe(str) {
    let new_str = str
    for(var i=0;i<new_str.length-1;i++){
        if (new_str[i]==new_str[i+1]){
            new_str=new_str.slice(0, i) + new_str.slice(i + 1)
        }
    }
    return new_str
}
console.log(stringDedupe(str2))