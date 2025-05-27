package algorithm;

/**
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 *
 * 如果不存在公共前缀，返回空字符串 ""。
 *
 *
 *
 * 示例 1：
 *
 * 输入：strs = ["flower","flow","flight"]
 * 输出："fl"
 * 示例 2：
 *
 * 输入：strs = ["dog","racecar","car"]
 * 输出：""
 * 解释：输入不存在公共前缀。
 *
 *
 * 提示：
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] 如果非空，则仅由小写英文字母组成
 */
public class 最长公共前缀 {
    public String longestStr(String[] s){
    if (s==null||s.length==0) return "";
        for (int i = 0; i < s[0].length(); i++) {
            char c = s[0].charAt(i);
            for (int j = 0; j < s.length; j++) {
                if (i>=s[j].length()||s[j].charAt(i)!=c){
                return s[0].substring(0,i);
                }
            }

        }
        return s[0];
    }
}

















