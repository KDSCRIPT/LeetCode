// Given a string s, reverse only all the vowels in the string and return it.

// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

// Example 1:

// Input: s = "hello"
// Output: "holle"
// Example 2:

// Input: s = "leetcode"
// Output: "leotcede"

// Constraints:

// 1 <= s.length <= 3 * 105
// s consist of printable ASCII characters.

//My solution(287/480 test cases passed)
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  let start_index = 0;
  let end_index = s.length - 1;
  let s1 = "";
  let start = s[start_index];
  let ending = s[end_index];
  while (start_index <= s.length - 1) {
    if (
      start === "a" ||
      start === "e" ||
      start === "i" ||
      start === "o" ||
      start === "u"
    ) {
      if (
        ending === "a" ||
        ending === "e" ||
        ending === "i" ||
        ending === "o" ||
        ending === "u"
      ) {
        let temp = start;
        start = ending;
        ending = temp;
        end_index--;
      }
    }
    s1 += start;
    start_index++;
    start = s[start_index];
    ending = s[end_index];
  }
  console.log(s1);
  return s1;
};

//The best answer I found in leetcode
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  vowel_stack = [];
  final_string = "";
  for (let i = 0; i < s.length; i++) {
    if (
      s[i] === "a" ||
      s[i] === "e" ||
      s[i] === "i" ||
      s[i] === "o" ||
      s[i] === "u" ||
      s[i] === "A" ||
      s[i] == "E" ||
      s[i] == "I" ||
      s[i] == "O" ||
      s[i] == "U"
    ) {
      vowel_stack.push(s[i]);
    }
  }
  for (let i = 0; i < s.length; i++) {
    if (
      s[i] === "a" ||
      s[i] === "e" ||
      s[i] === "i" ||
      s[i] === "o" ||
      s[i] === "u" ||
      s[i] === "A" ||
      s[i] == "E" ||
      s[i] == "I" ||
      s[i] == "O" ||
      s[i] == "U"
    ) {
      final_string += vowel_stack.pop();
    } else {
      final_string += s[i];
    }
  }
  return final_string;
};
