/*
Navicat MySQL Data Transfer

Source Server         : localtest
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : zhu_test

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2018-01-09 17:55:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add author', '7', 'add_author');
INSERT INTO `auth_permission` VALUES ('20', 'Can change author', '7', 'change_author');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete author', '7', 'delete_author');
INSERT INTO `auth_permission` VALUES ('22', 'Can add book', '8', 'add_book');
INSERT INTO `auth_permission` VALUES ('23', 'Can change book', '8', 'change_book');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete book', '8', 'delete_book');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for client_info
-- ----------------------------
DROP TABLE IF EXISTS `client_info`;
CREATE TABLE `client_info` (
  `address` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of client_info
-- ----------------------------
INSERT INTO `client_info` VALUES ('安徽中安', '13575752323', '123456', '1');
INSERT INTO `client_info` VALUES ('湖南常德', '15173659300', '430726zw', '3');
INSERT INTO `client_info` VALUES ('内蒙古呼市', '13805986830', '123456789', '4');
INSERT INTO `client_info` VALUES ('湖南衡阳', '18069888832', '123456789', '5');
INSERT INTO `client_info` VALUES ('i', 'i', 'i', '19');
INSERT INTO `client_info` VALUES ('o', 'o', 'o', '20');
INSERT INTO `client_info` VALUES ('p', 'p', 'p', '21');
INSERT INTO `client_info` VALUES ('ww', 'ww', 'ww', '22');
INSERT INTO `client_info` VALUES ('ttt', 'ttt', 'tt', '23');
INSERT INTO `client_info` VALUES ('z', 'z', 'z', '24');
INSERT INTO `client_info` VALUES ('x', 'x', 'x', '25');
INSERT INTO `client_info` VALUES ('c', 'c', 'c', '26');
INSERT INTO `client_info` VALUES ('v', 'v', 'v', '27');
INSERT INTO `client_info` VALUES ('n', 'n', 'n', '29');
INSERT INTO `client_info` VALUES ('m', 'm', 'm', '30');
INSERT INTO `client_info` VALUES ('9', '9', '9', '35');
INSERT INTO `client_info` VALUES ('9', '9', '9', '36');

-- ----------------------------
-- Table structure for devops_register
-- ----------------------------
DROP TABLE IF EXISTS `devops_register`;
CREATE TABLE `devops_register` (
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  `auto` int(11) NOT NULL AUTO_INCREMENT,
  `islogin` varchar(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`auto`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of devops_register
-- ----------------------------
INSERT INTO `devops_register` VALUES ('root', 'root ', 'admin', '1', '0');
INSERT INTO `devops_register` VALUES ('zhu', '', '1', '2', '0');
INSERT INTO `devops_register` VALUES ('zhuzhu', 'zhu', 'opt', '3', '0');
INSERT INTO `devops_register` VALUES ('lixiang', 'zz', 'opt', '4', '0');
INSERT INTO `devops_register` VALUES ('lili', 'lili', 'CTO', '6', '0');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'many_test', 'author');
INSERT INTO `django_content_type` VALUES ('8', 'many_test', 'book');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-12-25 07:21:29');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-12-25 07:21:36');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-12-25 07:21:38');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-12-25 07:21:38');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-12-25 07:21:39');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-12-25 07:21:39');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-12-25 07:21:40');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-12-25 07:21:40');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-12-25 07:21:41');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-12-25 07:21:41');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-12-25 07:21:41');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-12-25 07:21:41');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2017-12-25 07:21:42');
INSERT INTO `django_migrations` VALUES ('14', 'many_test', '0001_initial', '2018-01-03 05:43:08');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('dnifao5xwfm4kx23i4anlcsryfhqge7r', 'MjlkNTQ0NjAzZmQ0ZTBlZTVhMzY5NDY3YzgzZWYyMjIwYjc4ODYxMDp7InVzZXJuYW1lIjoiemh1emh1In0=', '2018-01-18 12:43:42');
INSERT INTO `django_session` VALUES ('nwim4zr00n7s1z8gcgol5ih7nf7cm51q', 'YTkxYmQ3MTk0NmI3YmVjMTQzY2VlMjUwNzcwOGEyYzYzZmYxNTI5Zjp7InVzZXJuYW1lIjoicm9vdCJ9', '2018-01-16 03:02:05');
INSERT INTO `django_session` VALUES ('vsgna464z9tnnah0l5i1ws8dsybwqaw3', 'MjlkNTQ0NjAzZmQ0ZTBlZTVhMzY5NDY3YzgzZWYyMjIwYjc4ODYxMDp7InVzZXJuYW1lIjoiemh1emh1In0=', '2018-01-08 08:26:13');

-- ----------------------------
-- Table structure for index_author
-- ----------------------------
DROP TABLE IF EXISTS `index_author`;
CREATE TABLE `index_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_author
-- ----------------------------
INSERT INTO `index_author` VALUES ('3', 'aa', 'bb');
INSERT INTO `index_author` VALUES ('4', 'aa', 'bb');
INSERT INTO `index_author` VALUES ('5', 'aa', 'bb');
INSERT INTO `index_author` VALUES ('6', 'aa', 'bb');
INSERT INTO `index_author` VALUES ('7', 'aa', 'bb');
INSERT INTO `index_author` VALUES ('8', 'vv', 'v');
INSERT INTO `index_author` VALUES ('9', 'vv', 'v');

-- ----------------------------
-- Table structure for index_book
-- ----------------------------
DROP TABLE IF EXISTS `index_book`;
CREATE TABLE `index_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_book
-- ----------------------------
INSERT INTO `index_book` VALUES ('4', 'ibk');
INSERT INTO `index_book` VALUES ('5', 'ibk');
INSERT INTO `index_book` VALUES ('6', 'ibk');
INSERT INTO `index_book` VALUES ('7', 'ii');
INSERT INTO `index_book` VALUES ('8', 'ii');
INSERT INTO `index_book` VALUES ('9', 'ii');
INSERT INTO `index_book` VALUES ('10', 'i');

-- ----------------------------
-- Table structure for index_book_author
-- ----------------------------
DROP TABLE IF EXISTS `index_book_author`;
CREATE TABLE `index_book_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_book_id` (`book_id`),
  KEY `index_author_id` (`author_id`),
  CONSTRAINT `index_author_id` FOREIGN KEY (`author_id`) REFERENCES `index_author` (`id`),
  CONSTRAINT `index_book_id` FOREIGN KEY (`book_id`) REFERENCES `index_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of index_book_author
-- ----------------------------
INSERT INTO `index_book_author` VALUES ('3', '8', '7');
INSERT INTO `index_book_author` VALUES ('4', '9', '8');
INSERT INTO `index_book_author` VALUES ('5', '10', '9');

-- ----------------------------
-- Table structure for many_test_author
-- ----------------------------
DROP TABLE IF EXISTS `many_test_author`;
CREATE TABLE `many_test_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of many_test_author
-- ----------------------------
INSERT INTO `many_test_author` VALUES ('23', 'nn', 'dd', 'qq@qq.com');
INSERT INTO `many_test_author` VALUES ('24', 'nn', 'dd', 'qq@qq.com');
INSERT INTO `many_test_author` VALUES ('25', 'nn', 'dd', 'qq@qq.com');
INSERT INTO `many_test_author` VALUES ('26', 'nn', 'dd', 'qq@qq.com');
INSERT INTO `many_test_author` VALUES ('27', 'nn', 'dd', 'qq@qq.com');

-- ----------------------------
-- Table structure for many_test_book
-- ----------------------------
DROP TABLE IF EXISTS `many_test_book`;
CREATE TABLE `many_test_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of many_test_book
-- ----------------------------
INSERT INTO `many_test_book` VALUES ('1', 'max');
INSERT INTO `many_test_book` VALUES ('2', 'maxi');
INSERT INTO `many_test_book` VALUES ('3', 'maxi');
INSERT INTO `many_test_book` VALUES ('4', 'maxi');
INSERT INTO `many_test_book` VALUES ('5', 'maxi');
INSERT INTO `many_test_book` VALUES ('6', 'maxi');
INSERT INTO `many_test_book` VALUES ('7', '111');

-- ----------------------------
-- Table structure for many_test_book_authors
-- ----------------------------
DROP TABLE IF EXISTS `many_test_book_authors`;
CREATE TABLE `many_test_book_authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `many_test_book_authors_book_id_author_id_5d963c3d_uniq` (`book_id`,`author_id`),
  KEY `many_test_book_authors_author_id_631fc548_fk_many_test_author_id` (`author_id`),
  CONSTRAINT `many_test_book_authors_author_id_631fc548_fk_many_test_author_id` FOREIGN KEY (`author_id`) REFERENCES `many_test_author` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `many_test_book_authors_book_id_442ba54c_fk_many_test_book_id` FOREIGN KEY (`book_id`) REFERENCES `many_test_book` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of many_test_book_authors
-- ----------------------------
INSERT INTO `many_test_book_authors` VALUES ('22', '2', '23');
INSERT INTO `many_test_book_authors` VALUES ('23', '3', '24');
INSERT INTO `many_test_book_authors` VALUES ('24', '4', '25');
INSERT INTO `many_test_book_authors` VALUES ('25', '5', '26');
INSERT INTO `many_test_book_authors` VALUES ('26', '6', '27');

-- ----------------------------
-- Table structure for membership
-- ----------------------------
DROP TABLE IF EXISTS `membership`;
CREATE TABLE `membership` (
  `person` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invite_reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `persons` (`person`),
  CONSTRAINT `persons` FOREIGN KEY (`person`) REFERENCES `person` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of membership
-- ----------------------------
INSERT INTO `membership` VALUES ('ggg', '48', 'mmmmmmmm');

-- ----------------------------
-- Table structure for module_detail
-- ----------------------------
DROP TABLE IF EXISTS `module_detail`;
CREATE TABLE `module_detail` (
  `module` varchar(255) DEFAULT NULL,
  `module_version` varchar(255) DEFAULT NULL,
  `module_date` varchar(255) DEFAULT NULL,
  `module_update` varchar(255) DEFAULT NULL,
  `additional` varchar(255) DEFAULT NULL,
  `module_in` varchar(255) DEFAULT NULL,
  `company_id` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `module` (`module`),
  KEY `module_2` (`module`),
  KEY `module_3` (`module`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COMMENT='zcell_module    == module_name';

-- ----------------------------
-- Records of module_detail
-- ----------------------------
INSERT INTO `module_detail` VALUES ('AS-K41100', '1.0.0.127', '11', '12', 'rrrrrrrrrrr', 'AlarmPlugin.dll', '01', '1');
INSERT INTO `module_detail` VALUES ('AS-K41100', '1.0.0.127', '11', '12', 'rrrrrrrrrrrrr', 'AlarmPlugin.dll', '01', '4');
INSERT INTO `module_detail` VALUES ('rr', 's', 's', 's', 's', 'ask-11001', 'r', '11');
INSERT INTO `module_detail` VALUES ('rr', 'g', 'g', 'g', 'g', 'g', 'r', '12');
INSERT INTO `module_detail` VALUES ('ww', '2', '2', '2', '2', 'aaa-44', 'www', '15');
INSERT INTO `module_detail` VALUES ('ww', '11', '11', '11', '1', 'as-rrrrr', 'www', '16');
INSERT INTO `module_detail` VALUES ('ww', '0', '0', '0', '0', 'as-00', 'www', '18');
INSERT INTO `module_detail` VALUES ('11', 's', 's', 'ooooo', 's', 'as-99', '09', '20');

-- ----------------------------
-- Table structure for online_server
-- ----------------------------
DROP TABLE IF EXISTS `online_server`;
CREATE TABLE `online_server` (
  `instance_ID` varchar(255) NOT NULL,
  `instance_name` varchar(255) NOT NULL,
  `out_net` varchar(255) NOT NULL,
  `inner_net` varchar(255) NOT NULL,
  `cpu` varchar(255) NOT NULL,
  `memory` varchar(255) NOT NULL,
  `createtime` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `SYS` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `deadtime` varchar(255) NOT NULL,
  `bandwidth` varchar(255) NOT NULL,
  `project` varchar(500) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `instance_ID_index` (`instance_ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of online_server
-- ----------------------------
INSERT INTO `online_server` VALUES ('d', 'd', 'd', 'd', 'd', 'd', 'sf', 'a', 'fa', 'af', 'af', 'fa', 'sf', 'fadfsff', '1');
INSERT INTO `online_server` VALUES ('t', 't', 't', 't', 't', 't', 't', 't', '', 't', 't', 't', 't', 't', '2');

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person` (
  `name` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`,`name`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of person
-- ----------------------------
INSERT INTO `person` VALUES ('ggg', '40');
INSERT INTO `person` VALUES ('test', '21');
INSERT INTO `person` VALUES ('zhu1', '17');

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `tes` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test
-- ----------------------------
INSERT INTO `test` VALUES ('565');

-- ----------------------------
-- Table structure for test_server
-- ----------------------------
DROP TABLE IF EXISTS `test_server`;
CREATE TABLE `test_server` (
  `instance_ID` varchar(255) NOT NULL,
  `instance_name` varchar(255) NOT NULL,
  `out_net` varchar(255) NOT NULL,
  `inner_net` varchar(255) NOT NULL,
  `cpu` varchar(255) NOT NULL,
  `memory` varchar(255) NOT NULL,
  `createtime` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `SYS` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `deadtime` varchar(255) NOT NULL,
  `bandwidth` varchar(255) NOT NULL,
  `project` varchar(500) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `instance_ID_index` (`instance_ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test_server
-- ----------------------------
INSERT INTO `test_server` VALUES ('12', '23', '11.11.11.11', '10.1.1.1', '4', '1028', '2017/11/11', 'test', 'tes_123', 'LINUX', '8080', '2018/11/11', '4', 'ALARMSERVER,ANGLER', '4');
INSERT INTO `test_server` VALUES ('', '', '', '', '2', '', '', '2', '2', '2', '2', '2', '', '2', '6');
INSERT INTO `test_server` VALUES ('3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '		3	', '7');
INSERT INTO `test_server` VALUES ('4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '			4', '8');
INSERT INTO `test_server` VALUES ('5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '	5		', '9');
INSERT INTO `test_server` VALUES ('6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '		6	', '10');
INSERT INTO `test_server` VALUES ('7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '		7	', '11');
INSERT INTO `test_server` VALUES ('8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '		8	', '12');
INSERT INTO `test_server` VALUES ('q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', '			q', '13');
INSERT INTO `test_server` VALUES ('w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '	w		', '14');
INSERT INTO `test_server` VALUES ('ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', 'ee', '		ee	', '15');
INSERT INTO `test_server` VALUES ('121', '11', '10.1.1.1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '11111', '18');
INSERT INTO `test_server` VALUES ('11', 'd', 'dd', '', '', '', '', '', '', '', '', '', '', 'sfsdfsfs', '20');
INSERT INTO `test_server` VALUES ('3333', '', '', '', '', '', '', '', '', '', '', '', '', '', '21');

-- ----------------------------
-- Table structure for update_test_server
-- ----------------------------
DROP TABLE IF EXISTS `update_test_server`;
CREATE TABLE `update_test_server` (
  `update_people` varchar(255) NOT NULL,
  `server` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `sys_variety` varchar(255) NOT NULL,
  `update_time` varchar(255) NOT NULL,
  `except_info` varchar(1000) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `online_offline` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of update_test_server
-- ----------------------------
INSERT INTO `update_test_server` VALUES ('LX', '10.16.25.1', 'test_web', 'linux', '2018-01-01T01:00', 'q', '85', 'online');
INSERT INTO `update_test_server` VALUES ('LX', '10.16.25.1', 'test_web', 'linux', '2018-02-01T01:00', '\'', '86', 'online');
INSERT INTO `update_test_server` VALUES ('ZZ', '10.16.25.1', 'test_web', 'windows', '2018-01-01T13:00', 'eqe', '87', 'offline');
INSERT INTO `update_test_server` VALUES ('ZZ', '10.16.25.1', 'test_web', 'linux', '2018-02-01T01:00', 'gg', '88', 'online');
INSERT INTO `update_test_server` VALUES ('LX', '10.16.25.1', 'test_wg', 'linux', '2018-01-01T01:00', 'fds', '89', 'online');

-- ----------------------------
-- Table structure for zcell_module
-- ----------------------------
DROP TABLE IF EXISTS `zcell_module`;
CREATE TABLE `zcell_module` (
  `zone` varchar(255) NOT NULL,
  `company_id` varchar(255) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `server_ip` varchar(255) NOT NULL,
  `server_name` varchar(255) NOT NULL,
  `node` varchar(255) NOT NULL COMMENT 'module_name is foreigh_key',
  `module_name` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `portv` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `zcell_nodes` (`module_name`,`company_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zcell_module
-- ----------------------------
INSERT INTO `zcell_module` VALUES ('cc', 'www', 'wccc', 'ccc', 'cc', 'cc', 'ww', 'cc', 'cc', '22');
INSERT INTO `zcell_module` VALUES ('gg', '09', 'xiaolx', '10.1.1.1', 'zcell1', 'ss', '11', '11', '11', '23');
INSERT INTO `zcell_module` VALUES ('shagndong province', '11', 'jx-ik', '1.1.1.1', 'zcell2', '222', 'as-88', '1', '2', '24');
