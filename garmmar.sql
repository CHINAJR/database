--创建数据库
CREATE DATABASE `school`;
USE `school`;
SHOW DATABASES;

CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `nickname` varchar(20) NOT NULL,
  `sex` char(1) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
  )DEFAULT CHARSET=utf8;

INSERT INTO `students` VALUE(3,'nike','ni','g',now());
INSERT INTO `students2` (`name`,`nickname`,`sex`,`time`) VALUE ('nike','ni','g',now());
INSERT INTO `students2` (`name`,`nickname`,`sex`,`time`) VALUES ('nike','ni','g',now()),('nike','ni','g',now());

SELECT `name`,`nickname` FROM  `students2`;

SELECT * FROM  `students2` WHERE `sex` = 'g' ORDER BY `id` DESC	LIMIT 0,2;
SELECT * FROM  `students2` WHERE `sex` = 'g' ORDER BY `id` DESC	LIMIT 2,2;--每页两条，偏移两条后
UPDATE `students2` SET `sex` = 'm' WHERE `name` = 'nike';
delete from `students2` where `sex` = 'n';

create  table `news`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `img_url` varchar(200) NULL,
  `content` varchar(2000) NOT NULL,
  `is_valid` smallint default 1,
  `created_at` datetime default NULL,
  `updated_at` datetime default NULL,
  `news_types` varchar(100) default '百家',
  `author` varchar(20) NULL,
  `view_count` int default 0,
  PRIMARY KEY (`id`)
  )DEFAULT CHARSET=utf8;

insert into `news`(`title`,`img_url`,`content`)values ('a11','ab1','abc'),('b11','bb1','bbc'),('c11','cb1','cbc'),('d11','db1','dbc'),('e11','eb1','ebc')

select * from `news` where `news_types` = '百家';

delete  from `news` where `id` = 15;

select * from `news` order by `id` desc;

select * from `news` order by `id` limit 5,5;--第二页


-- #orm
--
-- from testorm import engine
-- from testorm import News
-- News.metadata.create_all(engine)
