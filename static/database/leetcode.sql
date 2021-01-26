/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : mysql_demo

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 24/10/2020 23:39:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for leetcode
-- ----------------------------
DROP TABLE IF EXISTS `leetcode`;
CREATE TABLE `leetcode` (
  `question_id` bigint DEFAULT NULL,
  `title` text,
  `status` text,
  `difficulty` bigint DEFAULT NULL,
  `url` text,
  KEY `ix_leetcode_question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of leetcode
-- ----------------------------
BEGIN;
INSERT INTO `leetcode` VALUES (100347, '二叉树的最近公共祖先', NULL, 1, 'er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof');
INSERT INTO `leetcode` VALUES (100346, '二叉搜索树的最近公共祖先', NULL, 1, 'er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof');
INSERT INTO `leetcode` VALUES (100345, '求1+2+…+n', NULL, 2, 'qiu-12n-lcof');
INSERT INTO `leetcode` VALUES (100344, '股票的最大利润', NULL, 2, 'gu-piao-de-zui-da-li-run-lcof');
INSERT INTO `leetcode` VALUES (100343, '圆圈中最后剩下的数字', NULL, 1, 'yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100342, '平衡二叉树', NULL, 1, 'ping-heng-er-cha-shu-lcof');
INSERT INTO `leetcode` VALUES (100341, '扑克牌中的顺子', NULL, 1, 'bu-ke-pai-zhong-de-shun-zi-lcof');
INSERT INTO `leetcode` VALUES (100340, '把字符串转换成整数', NULL, 2, 'ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof');
INSERT INTO `leetcode` VALUES (100339, 'n个骰子的点数', NULL, 1, 'nge-tou-zi-de-dian-shu-lcof');
INSERT INTO `leetcode` VALUES (100338, '构建乘积数组', NULL, 2, 'gou-jian-cheng-ji-shu-zu-lcof');
INSERT INTO `leetcode` VALUES (100337, '队列的最大值', NULL, 2, 'dui-lie-de-zui-da-zhi-lcof');
INSERT INTO `leetcode` VALUES (100336, '滑动窗口的最大值', NULL, 1, 'hua-dong-chuang-kou-de-zui-da-zhi-lcof');
INSERT INTO `leetcode` VALUES (100335, '不用加减乘除做加法', NULL, 1, 'bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof');
INSERT INTO `leetcode` VALUES (100334, '丑数', NULL, 2, 'chou-shu-lcof');
INSERT INTO `leetcode` VALUES (100333, '二叉搜索树的第k大节点', NULL, 1, 'er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof');
INSERT INTO `leetcode` VALUES (100332, '最长不含重复字符的子字符串', NULL, 2, 'zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof');
INSERT INTO `leetcode` VALUES (100331, '缺失的数字', NULL, 1, 'que-shi-de-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100330, '左旋转字符串', NULL, 1, 'zuo-xuan-zhuan-zi-fu-chuan-lcof');
INSERT INTO `leetcode` VALUES (100329, '在排序数组中查找数字', NULL, 1, 'zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100328, '翻转单词顺序', NULL, 1, 'fan-zhuan-dan-ci-shun-xu-lcof');
INSERT INTO `leetcode` VALUES (100327, '礼物的最大价值', NULL, 2, 'li-wu-de-zui-da-jie-zhi-lcof');
INSERT INTO `leetcode` VALUES (100326, '两个链表的第一个公共节点', NULL, 1, 'liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof');
INSERT INTO `leetcode` VALUES (100325, '把数字翻译成字符串', NULL, 2, 'ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof');
INSERT INTO `leetcode` VALUES (100324, '和为s的连续正数序列', NULL, 1, 'he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof');
INSERT INTO `leetcode` VALUES (100323, '把数组排成最小的数', NULL, 2, 'ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof');
INSERT INTO `leetcode` VALUES (100322, '和为s的两个数字', NULL, 1, 'he-wei-sde-liang-ge-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100321, '数组中数字出现的次数', NULL, 2, 'shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof');
INSERT INTO `leetcode` VALUES (100320, '数组中数字出现的次数', NULL, 2, 'shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof');
INSERT INTO `leetcode` VALUES (100319, '二叉树的深度', NULL, 1, 'er-cha-shu-de-shen-du-lcof');
INSERT INTO `leetcode` VALUES (100318, '数组中的逆序对', NULL, 3, 'shu-zu-zhong-de-ni-xu-dui-lcof');
INSERT INTO `leetcode` VALUES (100317, '二叉树中和为某一值的路径', 'ac', 2, 'er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof');
INSERT INTO `leetcode` VALUES (100316, '第一个只出现一次的字符', NULL, 1, 'di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof');
INSERT INTO `leetcode` VALUES (100315, '二叉搜索树的后序遍历序列', 'ac', 2, 'er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof');
INSERT INTO `leetcode` VALUES (100314, '从上到下打印二叉树', 'ac', 2, 'cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof');
INSERT INTO `leetcode` VALUES (100313, '数字序列中某一位的数字', NULL, 2, 'shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100312, '从上到下打印二叉树', 'ac', 1, 'cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof');
INSERT INTO `leetcode` VALUES (100311, '从上到下打印二叉树', 'ac', 2, 'cong-shang-dao-xia-da-yin-er-cha-shu-lcof');
INSERT INTO `leetcode` VALUES (100310, '数组中出现次数超过一半的数字', 'ac', 1, 'shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100309, '1～n整数中1出现的次数', 'ac', 3, '1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof');
INSERT INTO `leetcode` VALUES (100308, '字符串的排列', 'ac', 2, 'zi-fu-chuan-de-pai-lie-lcof');
INSERT INTO `leetcode` VALUES (100307, '序列化二叉树', 'ac', 3, 'xu-lie-hua-er-cha-shu-lcof');
INSERT INTO `leetcode` VALUES (100306, '栈的压入、弹出序列', 'ac', 2, 'zhan-de-ya-ru-dan-chu-xu-lie-lcof');
INSERT INTO `leetcode` VALUES (100305, '二叉搜索树与双向链表', 'ac', 2, 'er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof');
INSERT INTO `leetcode` VALUES (100304, '连续子数组的最大和', 'ac', 1, 'lian-xu-zi-shu-zu-de-zui-da-he-lcof');
INSERT INTO `leetcode` VALUES (100303, '数据流中的中位数', 'ac', 3, 'shu-ju-liu-zhong-de-zhong-wei-shu-lcof');
INSERT INTO `leetcode` VALUES (100302, '包含min函数的栈', 'ac', 1, 'bao-han-minhan-shu-de-zhan-lcof');
INSERT INTO `leetcode` VALUES (100301, '最小的k个数', 'ac', 1, 'zui-xiao-de-kge-shu-lcof');
INSERT INTO `leetcode` VALUES (100300, '复杂链表的复制', 'ac', 2, 'fu-za-lian-biao-de-fu-zhi-lcof');
INSERT INTO `leetcode` VALUES (100299, '删除链表的节点', 'ac', 1, 'shan-chu-lian-biao-de-jie-dian-lcof');
INSERT INTO `leetcode` VALUES (100298, '反转链表', 'ac', 1, 'fan-zhuan-lian-biao-lcof');
INSERT INTO `leetcode` VALUES (100297, '正则表达式匹配', NULL, 3, 'zheng-ze-biao-da-shi-pi-pei-lcof');
INSERT INTO `leetcode` VALUES (100296, '打印从1到最大的n位数', 'ac', 1, 'da-yin-cong-1dao-zui-da-de-nwei-shu-lcof');
INSERT INTO `leetcode` VALUES (100295, '数值的整数次方', 'ac', 2, 'shu-zhi-de-zheng-shu-ci-fang-lcof');
INSERT INTO `leetcode` VALUES (100294, '链表中倒数第k个节点', 'ac', 1, 'lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof');
INSERT INTO `leetcode` VALUES (100293, '顺时针打印矩阵', 'ac', 1, 'shun-shi-zhen-da-yin-ju-zhen-lcof');
INSERT INTO `leetcode` VALUES (100292, '二进制中1的个数', 'ac', 1, 'er-jin-zhi-zhong-1de-ge-shu-lcof');
INSERT INTO `leetcode` VALUES (100291, '调整数组顺序使奇数位于偶数前面', 'ac', 1, 'diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof');
INSERT INTO `leetcode` VALUES (100290, '表示数值的字符串', 'ac', 2, 'biao-shi-shu-zhi-de-zi-fu-chuan-lcof');
INSERT INTO `leetcode` VALUES (100289, '对称的二叉树', 'ac', 1, 'dui-cheng-de-er-cha-shu-lcof');
INSERT INTO `leetcode` VALUES (100288, '二叉树的镜像', 'ac', 1, 'er-cha-shu-de-jing-xiang-lcof');
INSERT INTO `leetcode` VALUES (100287, '树的子结构', 'ac', 2, 'shu-de-zi-jie-gou-lcof');
INSERT INTO `leetcode` VALUES (100286, '合并两个排序的链表', 'ac', 1, 'he-bing-liang-ge-pai-xu-de-lian-biao-lcof');
INSERT INTO `leetcode` VALUES (100285, '剪绳子', 'ac', 2, 'jian-sheng-zi-ii-lcof');
INSERT INTO `leetcode` VALUES (100284, '剪绳子', 'ac', 2, 'jian-sheng-zi-lcof');
INSERT INTO `leetcode` VALUES (100283, '重建二叉树', 'ac', 2, 'zhong-jian-er-cha-shu-lcof');
INSERT INTO `leetcode` VALUES (100282, '从尾到头打印链表', 'ac', 1, 'cong-wei-dao-tou-da-yin-lian-biao-lcof');
INSERT INTO `leetcode` VALUES (100281, '机器人的运动范围', 'ac', 2, 'ji-qi-ren-de-yun-dong-fan-wei-lcof');
INSERT INTO `leetcode` VALUES (100280, '替换空格', 'ac', 1, 'ti-huan-kong-ge-lcof');
INSERT INTO `leetcode` VALUES (100279, '矩阵中的路径', 'ac', 2, 'ju-zhen-zhong-de-lu-jing-lcof');
INSERT INTO `leetcode` VALUES (100278, '旋转数组的最小数字', 'ac', 1, 'xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100277, '青蛙跳台阶问题', 'ac', 1, 'qing-wa-tiao-tai-jie-wen-ti-lcof');
INSERT INTO `leetcode` VALUES (100276, '二维数组中的查找', 'ac', 1, 'er-wei-shu-zu-zhong-de-cha-zhao-lcof');
INSERT INTO `leetcode` VALUES (100275, '数组中重复的数字', 'ac', 1, 'shu-zu-zhong-zhong-fu-de-shu-zi-lcof');
INSERT INTO `leetcode` VALUES (100274, '斐波那契数列', 'ac', 1, 'fei-bo-na-qi-shu-lie-lcof');
INSERT INTO `leetcode` VALUES (100273, '用两个栈实现队列', 'ac', 1, 'yong-liang-ge-zhan-shi-xian-dui-lie-lcof');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
