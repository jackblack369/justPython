CREATE TABLE IF NOT EXISTS rtdsp.demo1
(
    CORPORATION varchar(3) COMMENT '表头_法人主体',
    DAY_DT varchar(8) COMMENT '表头_批量日期',
    FK_CMBRH_KEY varchar(9) COMMENT '机构号',
    CM_OPR_NO varchar(12) COMMENT '操作员号',
    CMTLR_DB_TIMESTAMP decimal(15,0) COMMENT '时间戳',
    CM_EDER_CASH_CNT decimal(2,0) COMMENT '现金帐实不符次数',
    CM_EDER_VOD_CNT decimal(2,0) COMMENT '凭证帐实不符次数',
    CM_TLR_ACCL_BUSN_DATE varchar(8) COMMENT '关帐营业日期',
    CM_TLR_ACCL_TIME varchar(6) COMMENT '关帐时间',
    CM_AVL_DT varchar(8) COMMENT '柜员的有效期限',
    CM_SEQ_NO varchar(3) COMMENT '柜员序号',
    FILLER varchar(8) COMMENT 'FILLER',
    PRIMARY KEY(CORPORATION,DAY_DT) NOT ENFORCED
)
WITH(
    'connector'='starrocks', 
    'jdbc-url'='jdbc:mysql://172.18.244.74:18030', 
    'scan-url'='172.18.244.74:19030', 
    'load-url'='172.18.244.74:18030,172.18.244.75:18030,172.18.244.75:18030', 
    'username'='root', 
    'password'='datacanvas', 
    'database-name'='rtdsp', 
    'table-name'='demo1' 
);
