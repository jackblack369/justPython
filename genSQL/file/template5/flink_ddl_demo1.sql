CREATE TABLE IF NOT EXISTS RTDSP.DEMO1
(
    CORPORATION VARCHAR(3) COMMENT '表头_法人主体',
    DAY_DT VARCHAR(8) COMMENT '表头_批量日期',
    FK_CMBRH_KEY VARCHAR(9) COMMENT '机构号',
    CM_OPR_NO VARCHAR(12) COMMENT '操作员号',
    CMTLR_DB_TIMESTAMP DECIMAL(15,0) COMMENT '时间戳',
    CM_EDER_CASH_CNT DECIMAL(2,0) COMMENT '现金帐实不符次数',
    CM_EDER_VOD_CNT DECIMAL(2,0) COMMENT '凭证帐实不符次数',
    CM_TLR_ACCL_BUSN_DATE VARCHAR(8) COMMENT '关帐营业日期',
    CM_TLR_ACCL_TIME VARCHAR(6) COMMENT '关帐时间',
    CM_AVL_DT VARCHAR(8) COMMENT '柜员的有效期限',
    CM_SEQ_NO VARCHAR(3) COMMENT '柜员序号',
    FILLER VARCHAR(8) COMMENT 'FILLER',
    PRIMARY KEY(CORPORATION,DAY_DT) NOT ENFORCED
)
WITH(
    'connector' = 'kafka',
    'topic' = 'demo1',
    'properties.bootstrap.servers' = '172.18.244.74:9092,172.18.244.75:9092,172.18.244.76:9092',
    'properties.group.id' = 'sqlGroup',
    'scan.startup.mode' = 'earliest-offset',
    'format' = 'json'
);
