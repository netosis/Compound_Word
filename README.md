# Compound_Word
The following code finds the <b><u>Longest</u></b> and the <b><u>Second Longest</u></b> <u><i>Compound Word</i></u> from the given file.

(Note:- Here a <b>COMPOUNDED WORD</b> is a word that can be constructed by concatenating only the shorter words also found in the same file)

The files that have been used for the code have words:
<ul>
  <li>alphabetically sorted words</li>
  <li>one word per line without any spaces</li>
  <li>all the words are in lower case</li>

<h2>Approach</h2>
The approach is to find a way to split the bigger word into smaller words and check for each word individually. This was done by dividing the word into two parts. The word would be divided into these two parts again and again until the second part of the word has 0 length. When this happens the code would have seperated all the different words present in the compounded word if those seperate words were also present in the file.<br>
This would be accomplished by creating a recursive function that divides the word into those two parts. When the first part is found to be in the file, then it recursively calls the second part and divides it again and again. This function returns True if the word is a compuond word where all the words that it is made up of is in the file else it returns false.
<h2>Running The Code</h2>

<ul>
  <li>To run the code you should have the the files containing the words in the same folder as that of the location of the code being saved.</li>
  <li>At the 4th line of the code you need to replace the file name in place of the "Input_02.txt"</li>
</ul>

<h2>Working of the Code</h2>

<ul>
  <li><b>Time</b> library is used for keeping track of the time that the code is running for</li>
  <li>The data in the files is read and stored in a list and a set.</li>
  <ul>
    <li>The data stored in list is sorted as per the word lengths in ascending order </li>
    <li>The same data is stored in a 'Set' to help with the searching in of the presenece of words in the file</li>
  </ul>
  <li>A function named <b>Checker</b> is created which and used to check wheather the given word is a compound word or not</li>
  <ul>
    <li>This function takes a word and the set with all the different words as it's parameters</li>
    <li>It splits the word in two parts, that is the 'pre' that is the prefix and 'suff' that is the suffix</li>
    <li>This fucntion returns True if both the pre and suff are present in the set else it returns False </li>
  </ul>
  <li>A loop is initiated to iterate through all the words in the list and check for the compound words</li>
  <li>When a word is found to be a compound word using the function, the length of the word is compared with the vairable 'longest' and 's_longest'</li>
  <ul>
    <li>If the length is greater than 'largest' then 's_largest' becomes 'largest' and 'largest' becomes that word which it was compared to</li>
    <li>If the length is the greather than 's_largest' then 's_largest' becomes the word that it was compared to</li>
  </ul>
  <li>After the loop ends, the largest and the second largest compound words are printed with the time taken as follows:-</li>
  ![image](https://github.com/netosis/Compound_Word/assets/82317842/71b09a70-ba16-4f09-bf90-17030f0e4dcc)

</ul>
<!-- <ul>
  <li>The <b>Time</b> library has been imported to get the time taken by the code to run.</li>
  <ul>
    <li>We initate the time in the 'start_time' variable, to keep track of the time when the code is running</li>
  </ul>
  <li>Now, the file is opened in the 'flie' variable using the 'open' function</li>
  <li>After opening the file the </li> -->
