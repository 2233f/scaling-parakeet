-- 创建数据库
create database if not exists dataAdmin character set utf8 collate utf8_general_ci;

-- 进入创建的数据库
use dataAdmin;

-- 创建后台员工管理
create table if not exists employee(
	`emp_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '员工编号，自增主键',
 	`emp_name` varchar(50) NOT NULL COMMENT '员工姓名',
 	`sex` varchar(10) NOT NULL COMMENT '性别',
 	`user` varchar(50) not null comment '账号',
 	`password` varchar(50) not null comment '密码',
 	`create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '入职时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='员工信息表';


-- 创建商品管理表
create table if not exists merchandise(
	`merchandise_id` int(11) NOT NULL auto_increment PRIMARY key  COMMENT '商品编号，自增主键',
 	`merchandise_name` varchar(50) NOT NULL COMMENT '商品名称',
 	`price` varchar(10) NOT NULL COMMENT '商品单价',
 	`nums` varchar(10) not null comment '数量'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品信息表';