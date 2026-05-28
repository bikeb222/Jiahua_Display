# omsdata Tables Over 1000 Rows

Generated at: 2026-04-11 10:48:31

Scope: user tables in `[omsdata]` with metadata row count greater than `1000`.

Safety note: this file was generated with read-only metadata SELECT queries only. The queries read SQL Server system metadata from `sys.tables`, `sys.schemas`, `sys.partitions`, `sys.columns`, `sys.types`, `sys.default_constraints`, `sys.computed_columns`, `sys.indexes`, and `sys.index_columns`. No `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, or `DROP` statements were executed.

Row count source: `sys.partitions` rows for heap / clustered index metadata. This avoids running `COUNT(*)` over business data tables.

Tables found: `60`

## Table List

| # | Table | Rows | Columns | Primary Key |
|---:|---|---:|---:|---|
| 1 | `[dbo].[invt_log]` | 2129307 | 37 | `Id` |
| 2 | `[dbo].[sys_log]` | 1429169 | 12 | `Id` |
| 3 | `[dbo].[cus_invt]` | 1426317 | 9 |  |
| 4 | `[dbo].[ord_log]` | 822247 | 39 | `Id` |
| 5 | `[dbo].[prt_log]` | 619188 | 8 |  |
| 6 | `[dbo].[invoice]` | 214212 | 48 | `Id` |
| 7 | `[dbo].[so_divs]` | 200463 | 18 | `Id` |
| 8 | `[dbo].[bnk_chks]` | 193377 | 13 |  |
| 9 | `[dbo].[ins_data]` | 183570 | 49 | `Id` |
| 10 | `[dbo].[ins_divs]` | 183568 | 18 | `Id` |
| 11 | `[dbo].[insdat2e]` | 183568 | 216 |  |
| 12 | `[dbo].[omsphead]` | 179087 | 74 |  |
| 13 | `[dbo].[bin_pur]` | 108183 | 14 |  |
| 14 | `[dbo].[plog]` | 107404 | 54 | `Id` |
| 15 | `[dbo].[order2e]` | 91674 | 216 |  |
| 16 | `[dbo].[proddesc]` | 89684 | 32 |  |
| 17 | `[dbo].[orders]` | 68624 | 109 | `Id` |
| 18 | `[dbo].[iadj_log]` | 59655 | 42 | `BAT_NUM`, `NT_NUM` |
| 19 | `[dbo].[bin_invs]` | 55423 | 10 |  |
| 20 | `[dbo].[bnk_rlog]` | 52513 | 20 |  |
| 21 | `[dbo].[zipfile]` | 42620 | 3 |  |
| 22 | `[dbo].[cus_ssm]` | 38000 | 30 | `Id` |
| 23 | `[dbo].[iadjfile]` | 33533 | 11 | `BAT_NUM` |
| 24 | `[dbo].[cus_bls]` | 30509 | 17 |  |
| 25 | `[dbo].[bin_file]` | 29500 | 28 |  |
| 26 | `[dbo].[bnk_dpst]` | 28902 | 16 |  |
| 27 | `[dbo].[bnk_cldp]` | 28381 | 12 |  |
| 28 | `[dbo].[msc_file]` | 27947 | 5 |  |
| 29 | `[dbo].[product_sync_backup_20241219]` | 27494 | 7 |  |
| 30 | `[dbo].[inv_divs]` | 25840 | 17 |  |
| 31 | `[dbo].[inv_detl]` | 25837 | 24 | `Id` |
| 32 | `[dbo].[inv_note]` | 25837 | 15 | `Id` |
| 33 | `[dbo].[prod_sls]` | 25592 | 110 |  |
| 34 | `[dbo].[inv_upc]` | 23245 | 4 |  |
| 35 | `[dbo].[inv_data]` | 20080 | 61 | `Id` |
| 36 | `[dbo].[apmtnote]` | 19660 | 4 |  |
| 37 | `[dbo].[bnk_clck]` | 18387 | 6 |  |
| 38 | `[dbo].[pbl_dist]` | 17369 | 10 |  |
| 39 | `[dbo].[product_sync]` | 17223 | 7 | `PROD_CD` |
| 40 | `[dbo].[acct_mst]` | 17216 | 15 | `Id` |
| 41 | `[dbo].[cus_divs]` | 17201 | 18 | `Id` |
| 42 | `[dbo].[customer]` | 17130 | 93 | `Id` |
| 43 | `[dbo].[cus_sls]` | 16992 | 39 |  |
| 44 | `[dbo].[cus_crd]` | 16755 | 14 | `Id` |
| 45 | `[dbo].[pbl_trs]` | 16703 | 16 |  |
| 46 | `[dbo].[inv]` | 16547 | 137 | `Id` |
| 47 | `[dbo].[pbl_ins]` | 15994 | 20 |  |
| 48 | `[dbo].[bnk_pmt]` | 14307 | 18 |  |
| 49 | `[dbo].[bol_log]` | 11259 | 19 |  |
| 50 | `[dbo].[dvf_chg]` | 9269 | 5 |  |
| 51 | `[dbo].[custdesc]` | 6747 | 33 |  |
| 52 | `[dbo].[qtn_log]` | 6549 | 24 |  |
| 53 | `[dbo].[chk_note]` | 6515 | 9 |  |
| 54 | `[dbo].[poshpf]` | 5340 | 44 | `PK_NUM` |
| 55 | `[dbo].[acctpbl]` | 5337 | 34 |  |
| 56 | `[dbo].[pur_ord]` | 5283 | 69 | `Id` |
| 57 | `[dbo].[bnk_cltr]` | 4014 | 13 |  |
| 58 | `[dbo].[exc_whs]` | 3721 | 32 | `ID` |
| 59 | `[dbo].[invs_lnt]` | 2758 | 5 | `Id` |
| 60 | `[dbo].[shp_ld]` | 2118 | 45 |  |

## 1. `[dbo].[invt_log]`

- Rows: `2129307`
- Columns: `37`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `LOG_DT` | `int` | YES |  |  | `` | `` |
| 2 | `LOG_TIME` | `int` | YES |  |  | `` | `` |
| 3 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 4 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 5 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 6 | `PROD_CD` | `char(21)` | YES |  |  | `` | `` |
| 7 | `PROD_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `UNIT_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `REAL_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `LOG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `PROD_COMP` | `char(1)` | YES |  |  | `` | `` |
| 14 | `TERM_LN` | `tinyint` | YES |  |  | `` | `` |
| 15 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `UT_DISC` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `COMM_LN` | `decimal(8,0)` | YES |  |  | `` | `` |
| 18 | `ORD_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 19 | `NT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 20 | `UT_SER` | `char(1)` | YES |  |  | `` | `` |
| 21 | `PROD_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `UT_DESC` | `char(60)` | YES |  |  | `` | `` |
| 23 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 24 | `TAX_IND` | `char(1)` | YES |  |  | `` | `` |
| 25 | `UT_NT` | `char(1)` | YES |  |  | `` | `` |
| 26 | `SO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `DISC_LINE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `PC_UNIT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `DEF_UT` | `char(2)` | YES |  |  | `` | `` |
| 30 | `REF_NUM` | `char(15)` | YES |  |  | `` | `` |
| 31 | `ORD_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 32 | `ORD_NT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 33 | `BONUS_PRS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 34 | `PO_NUM` | `char(20)` | YES |  |  | `` | `` |
| 35 | `Id` | `int` | NO | YES | YES | `` | `` |
| 36 | `LID` | `char(40)` | YES |  |  | `` | `` |
| 37 | `OLD_COMM_LN` | `int` | YES |  |  | `` | `` |

## 2. `[dbo].[sys_log]`

- Rows: `1429169`
- Columns: `12`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `COMPNO` | `tinyint` | NO |  |  | `` | `` |
| 2 | `SYS_DATE` | `int` | NO |  |  | `` | `` |
| 3 | `SYS_TM` | `int` | NO |  |  | `` | `` |
| 4 | `FILE_ID` | `char(2)` | YES |  |  | `` | `` |
| 5 | `REC_ID` | `char(16)` | YES |  |  | `` | `` |
| 6 | `REC_ID2` | `tinyint` | YES |  |  | `` | `` |
| 7 | `FILE_CFG` | `char(1)` | YES |  |  | `` | `` |
| 8 | `PROCESSOR` | `char(60)` | YES |  |  | `` | `` |
| 9 | `FILE_UPDT` | `char(1)` | YES |  |  | `` | `` |
| 10 | `Id` | `int` | NO | YES | YES | `` | `` |
| 11 | `SOURCE` | `char(20)` | YES |  |  | `` | `` |
| 12 | `COMM_LN` | `int` | NO |  |  | `((0))` | `` |

## 3. `[dbo].[cus_invt]`

- Rows: `1426317`
- Columns: `9`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 3 | `PRICE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 4 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 6 | `INVS_NUM` | `int` | YES |  |  | `` | `` |
| 7 | `INVS_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 9 | `CUS_PROD` | `char(21)` | YES |  |  | `` | `` |

## 4. `[dbo].[ord_log]`

- Rows: `822247`
- Columns: `39`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `OLG_DT` | `int` | YES |  |  | `` | `` |
| 2 | `OLG_TIME` | `decimal(8,0)` | YES |  |  | `` | `` |
| 3 | `ORD_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 4 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 5 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `INVS_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 7 | `PROD_CD` | `char(21)` | YES |  |  | `` | `` |
| 8 | `ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `CAN_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `UNIT_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `PROD_COMP` | `char(1)` | YES |  |  | `` | `` |
| 12 | `COMM_LN` | `decimal(8,0)` | YES |  |  | `` | `` |
| 13 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `INVS_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `PCK_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `SHIP_DT` | `int` | YES |  |  | `` | `` |
| 17 | `NT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 18 | `UT_NT` | `char(1)` | YES |  |  | `` | `` |
| 19 | `UT_SER` | `char(1)` | YES |  |  | `` | `` |
| 20 | `UT_DESC` | `char(60)` | YES |  |  | `` | `` |
| 21 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 22 | `TAX_IND` | `char(1)` | YES |  |  | `` | `` |
| 23 | `CAN_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 24 | `LOG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `SALE_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `DISC_LINE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `PC_UNIT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `DEF_UT` | `char(2)` | YES |  |  | `` | `` |
| 29 | `REF_NUM` | `char(12)` | YES |  |  | `` | `` |
| 30 | `BO_QTY` | `decimal(8,0)` | YES |  |  | `` | `` |
| 31 | `LOT_NUM` | `char(20)` | YES |  |  | `` | `` |
| 32 | `PUR_NUM` | `char(12)` | YES |  |  | `` | `` |
| 33 | `POR_NT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 34 | `ORD_NT_KEY` | `tinyint` | YES |  |  | `` | `` |
| 35 | `BONUS_PRS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 36 | `Id` | `int` | NO | YES | YES | `` | `` |
| 37 | `PROMOTION_LNT_NUM` | `int` | YES |  |  | `` | `` |
| 38 | `CRV_LNT_NUM` | `int` | YES |  |  | `` | `` |
| 40 | `OLD_COMM_LN` | `decimal(8,0)` | YES |  |  | `` | `` |

## 5. `[dbo].[prt_log]`

- Rows: `619188`
- Columns: `8`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PRT_DT` | `int` | NO |  |  | `` | `` |
| 2 | `PRT_TM` | `int` | NO |  |  | `` | `` |
| 3 | `PRT_TYPE` | `smallint` | NO |  |  | `` | `` |
| 4 | `FILE_NUM` | `char(15)` | NO |  |  | `` | `` |
| 5 | `FILE_CD` | `tinyint` | NO |  |  | `` | `` |
| 6 | `FORM_CD` | `tinyint` | YES |  |  | `` | `` |
| 7 | `PRT_BY` | `char(8)` | YES |  |  | `` | `` |
| 8 | `RES_FD` | `char(5)` | YES |  |  | `` | `` |

## 6. `[dbo].[invoice]`

- Rows: `214212`
- Columns: `48`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 3 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 4 | `INVS_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 5 | `INVS_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `PAID_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `INVS_TAX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `TAX_RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `MISC_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 13 | `SALES_NUM` | `char(5)` | YES |  |  | `` | `` |
| 14 | `SALES_NUM2` | `char(4)` | YES |  |  | `` | `` |
| 15 | `INVS_TM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 16 | `INVS_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `HOLD_DAYS` | `tinyint` | YES |  |  | `` | `` |
| 18 | `ACT_NUM` | `tinyint` | YES |  |  | `` | `` |
| 19 | `PROCESSOR` | `char(10)` | YES |  |  | `` | `` |
| 20 | `COMM_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `COMM_AMT2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `COMM_RT2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `CHK_NUM` | `int` | YES |  |  | `` | `` |
| 25 | `COMM_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `INVS_TYPE` | `char(2)` | YES |  |  | `` | `` |
| 27 | `PROC_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 28 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 29 | `CHT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 30 | `CHT_NUM_2` | `decimal(8,0)` | YES |  |  | `` | `` |
| 31 | `UPDT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 32 | `UPDT_BY` | `char(8)` | YES |  |  | `` | `` |
| 33 | `TAXABLE_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 34 | `TERMS_DAY` | `decimal(5,0)` | YES |  |  | `` | `` |
| 35 | `TERMS_COD` | `char(1)` | YES |  |  | `` | `` |
| 36 | `TERM_DESC` | `char(15)` | YES |  |  | `` | `` |
| 37 | `PROC_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 38 | `SALES_NUM3` | `char(4)` | YES |  |  | `` | `` |
| 39 | `SALES_NUM4` | `char(4)` | YES |  |  | `` | `` |
| 40 | `COMM_AMT3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 41 | `COMM_RT3` | `decimal(5,2)` | YES |  |  | `` | `` |
| 42 | `COMM_AMT4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 43 | `COMM_RT4` | `decimal(5,2)` | YES |  |  | `` | `` |
| 44 | `PCODE` | `char(21)` | YES |  |  | `` | `` |
| 45 | `EARN_BONUS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 46 | `USED_BONUS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 47 | `BONUS_BACK` | `decimal(15,4)` | YES |  |  | `` | `` |
| 48 | `Id` | `int` | NO | YES | YES | `` | `` |

## 7. `[dbo].[so_divs]`

- Rows: `200463`
- Columns: `18`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ORD_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 4 | `DIV_CD` | `char(10)` | YES |  |  | `` | `` |
| 5 | `PRJ_CD` | `char(10)` | YES |  |  | `` | `` |
| 6 | `JOB_CD` | `char(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_CD` | `char(10)` | YES |  |  | `` | `` |
| 8 | `CLASS_CD` | `char(20)` | YES |  |  | `` | `` |
| 9 | `REG_CD` | `char(10)` | YES |  |  | `` | `` |
| 10 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 11 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `CHT_NUM2` | `int` | YES |  |  | `` | `` |
| 13 | `CHT_NUM3` | `int` | YES |  |  | `` | `` |
| 14 | `RSV_1` | `decimal(21,3)` | YES |  |  | `` | `` |
| 15 | `RSV_2` | `decimal(21,3)` | YES |  |  | `` | `` |
| 16 | `RSV_3` | `char(60)` | YES |  |  | `` | `` |
| 17 | `RSV_4` | `char(60)` | YES |  |  | `` | `` |
| 18 | `Id` | `int` | NO | YES | YES | `` | `` |

## 8. `[dbo].[bnk_chks]`

- Rows: `193377`
- Columns: `13`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `DEP_DT` | `int` | YES |  |  | `` | `` |
| 2 | `BANK_NUM` | `tinyint` | YES |  |  | `` | `` |
| 3 | `DEP_NUM` | `int` | YES |  |  | `` | `` |
| 4 | `CHK_NUM` | `decimal(21,3)` | YES |  |  | `` | `` |
| 5 | `INVS_NUM` | `char(10)` | YES |  |  | `` | `` |
| 6 | `INVS_CD` | `tinyint` | YES |  |  | `` | `` |
| 7 | `CHK_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 9 | `BUS_CD` | `int` | YES |  |  | `` | `` |
| 10 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 11 | `INVS_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 12 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 13 | `DEP_DT1` | `char(10)` | YES |  |  | `` | `` |

## 9. `[dbo].[ins_data]`

- Rows: `183570`
- Columns: `49`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `ORDER_NO` | `int` | YES |  |  | `` | `` |
| 3 | `ORDER_DT` | `int` | YES |  |  | `` | `` |
| 4 | `SP_SM_ADR` | `char(1)` | YES |  |  | `` | `` |
| 5 | `PO_NUM` | `char(20)` | YES |  |  | `` | `` |
| 6 | `NUM_CTL` | `smallint` | YES |  |  | `` | `` |
| 7 | `SHIP_DT` | `int` | YES |  |  | `` | `` |
| 8 | `CC_PRINT` | `tinyint` | YES |  |  | `` | `` |
| 9 | `SP_ADR` | `char(60)` | YES |  |  | `` | `` |
| 10 | `SP_ADR_2` | `char(60)` | YES |  |  | `` | `` |
| 11 | `SP_ADR_22` | `char(60)` | YES |  |  | `` | `` |
| 12 | `SP_ADR_3` | `char(60)` | YES |  |  | `` | `` |
| 13 | `SP_CITY` | `char(40)` | YES |  |  | `` | `` |
| 14 | `SP_STATE` | `char(15)` | YES |  |  | `` | `` |
| 15 | `SP_ZIP` | `char(15)` | YES |  |  | `` | `` |
| 16 | `NT_SEL` | `char(1)` | YES |  |  | `` | `` |
| 17 | `ATTN` | `char(30)` | YES |  |  | `` | `` |
| 18 | `SHIP_DESC` | `char(15)` | YES |  |  | `` | `` |
| 19 | `BK_INVS` | `int` | YES |  |  | `` | `` |
| 20 | `FOB_DESC` | `char(15)` | YES |  |  | `` | `` |
| 21 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 22 | `INVS_TTL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `INVS_BAL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `MISC_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `HNDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `INVS_TAX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 28 | `STR_NUM` | `char(12)` | YES |  |  | `` | `` |
| 29 | `PACK_PRT` | `smallint` | YES |  |  | `` | `` |
| 30 | `INVS_PRT` | `smallint` | YES |  |  | `` | `` |
| 31 | `REF_NUM` | `char(20)` | YES |  |  | `` | `` |
| 32 | `PRT_SP` | `char(1)` | YES |  |  | `` | `` |
| 33 | `SOUR_DESC` | `char(8)` | YES |  |  | `` | `` |
| 34 | `SP_ADR_CN` | `char(40)` | YES |  |  | `` | `` |
| 35 | `CURRENCY` | `char(10)` | YES |  |  | `` | `` |
| 36 | `EXC_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `SHIP_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `AUTHRZ_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `EMAIL_ADR` | `char(100)` | YES |  |  | `` | `` |
| 40 | `EMAIL_IND` | `char(2)` | YES |  |  | `` | `` |
| 41 | `COD_CASH` | `char(1)` | YES |  |  | `` | `` |
| 42 | `TRK_NUM` | `char(30)` | YES |  |  | `` | `` |
| 43 | `ORDER_BY` | `char(10)` | YES |  |  | `` | `` |
| 44 | `CUS_SHIP_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 45 | `DISC_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 46 | `SP_CUS_NM` | `char(60)` | YES |  |  | `` | `` |
| 47 | `SOLD_TO` | `char(50)` | YES |  |  | `` | `` |
| 48 | `BL_NUM` | `char(30)` | YES |  |  | `` | `` |
| 49 | `Id` | `int` | NO | YES | YES | `` | `` |

## 10. `[dbo].[ins_divs]`

- Rows: `183568`
- Columns: `18`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 4 | `DIV_CD` | `char(10)` | YES |  |  | `` | `` |
| 5 | `PRJ_CD` | `char(10)` | YES |  |  | `` | `` |
| 6 | `JOB_CD` | `char(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_CD` | `char(10)` | YES |  |  | `` | `` |
| 8 | `CLASS_CD` | `char(20)` | YES |  |  | `` | `` |
| 9 | `REG_CD` | `char(10)` | YES |  |  | `` | `` |
| 10 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 11 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `CHT_NUM2` | `int` | YES |  |  | `` | `` |
| 13 | `CHT_NUM3` | `int` | YES |  |  | `` | `` |
| 14 | `RSV_1` | `decimal(21,3)` | YES |  |  | `` | `` |
| 15 | `RSV_2` | `decimal(21,3)` | YES |  |  | `` | `` |
| 16 | `RSV_3` | `char(60)` | YES |  |  | `` | `` |
| 17 | `RSV_4` | `char(60)` | YES |  |  | `` | `` |
| 18 | `Id` | `int` | NO | YES | YES | `` | `` |

## 11. `[dbo].[insdat2e]`

- Rows: `183568`
- Columns: `216`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `PO_NUM` | `varchar(22)` | YES |  |  | `` | `` |
| 3 | `PO_DT` | `int` | YES |  |  | `` | `` |
| 4 | `PURPOSE` | `varchar(2)` | YES |  |  | `` | `` |
| 5 | `PO_TYPE` | `varchar(2)` | YES |  |  | `` | `` |
| 6 | `BATCH_NUM` | `varchar(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_NUM` | `varchar(30)` | YES |  |  | `` | `` |
| 8 | `VEN_ID` | `varchar(20)` | YES |  |  | `` | `` |
| 9 | `SHP_DC_NUM` | `varchar(20)` | YES |  |  | `` | `` |
| 10 | `SLD_CUS_ID` | `varchar(20)` | YES |  |  | `` | `` |
| 11 | `INTERNAL_PO` | `varchar(20)` | YES |  |  | `` | `` |
| 12 | `OUR_TERM_CD` | `varchar(5)` | YES |  |  | `` | `` |
| 13 | `DISC_PER` | `varchar(8)` | YES |  |  | `` | `` |
| 14 | `DISC_DUE_DT` | `varchar(8)` | YES |  |  | `` | `` |
| 15 | `DISC_DAYS_DUE` | `varchar(4)` | YES |  |  | `` | `` |
| 16 | `NET_DUE_DT` | `varchar(8)` | YES |  |  | `` | `` |
| 17 | `NET_DAYS_DUE` | `varchar(4)` | YES |  |  | `` | `` |
| 18 | `RSV_1` | `char(35)` | YES |  |  | `` | `` |
| 19 | `RSV_2` | `char(35)` | YES |  |  | `` | `` |
| 20 | `RSV_3` | `char(35)` | YES |  |  | `` | `` |
| 21 | `RSV_4` | `char(35)` | YES |  |  | `` | `` |
| 22 | `RSV_5` | `char(35)` | YES |  |  | `` | `` |
| 23 | `RSV_6` | `char(35)` | YES |  |  | `` | `` |
| 24 | `RSV_7` | `char(35)` | YES |  |  | `` | `` |
| 25 | `RSV_8` | `char(35)` | YES |  |  | `` | `` |
| 26 | `RSV_9` | `char(35)` | YES |  |  | `` | `` |
| 27 | `RSV_10` | `char(35)` | YES |  |  | `` | `` |
| 28 | `RSV_11` | `char(35)` | YES |  |  | `` | `` |
| 29 | `RSV_12` | `char(35)` | YES |  |  | `` | `` |
| 30 | `RSV_13` | `char(35)` | YES |  |  | `` | `` |
| 31 | `RSV_14` | `char(35)` | YES |  |  | `` | `` |
| 32 | `RSV_15` | `char(35)` | YES |  |  | `` | `` |
| 33 | `RSV_16` | `char(35)` | YES |  |  | `` | `` |
| 34 | `RSV_17` | `char(35)` | YES |  |  | `` | `` |
| 35 | `RSV_18` | `char(35)` | YES |  |  | `` | `` |
| 36 | `RSV_19` | `char(35)` | YES |  |  | `` | `` |
| 37 | `RSV_20` | `char(35)` | YES |  |  | `` | `` |
| 38 | `RSV_21` | `char(35)` | YES |  |  | `` | `` |
| 39 | `RSV_22` | `char(35)` | YES |  |  | `` | `` |
| 40 | `RSV_23` | `char(35)` | YES |  |  | `` | `` |
| 41 | `RSV_24` | `char(35)` | YES |  |  | `` | `` |
| 42 | `RSV_25` | `char(35)` | YES |  |  | `` | `` |
| 43 | `RSV_26` | `char(35)` | YES |  |  | `` | `` |
| 44 | `RSV_27` | `char(35)` | YES |  |  | `` | `` |
| 45 | `RSV_28` | `char(35)` | YES |  |  | `` | `` |
| 46 | `RSV_29` | `char(35)` | YES |  |  | `` | `` |
| 47 | `RSV_30` | `char(35)` | YES |  |  | `` | `` |
| 48 | `RSV_31` | `char(35)` | YES |  |  | `` | `` |
| 49 | `RSV_32` | `char(35)` | YES |  |  | `` | `` |
| 50 | `RSV_33` | `char(35)` | YES |  |  | `` | `` |
| 51 | `RSV_34` | `char(35)` | YES |  |  | `` | `` |
| 52 | `RSV_35` | `char(35)` | YES |  |  | `` | `` |
| 53 | `RSV_36` | `char(35)` | YES |  |  | `` | `` |
| 54 | `RSV_37` | `char(35)` | YES |  |  | `` | `` |
| 55 | `RSV_38` | `char(35)` | YES |  |  | `` | `` |
| 56 | `RSV_39` | `char(35)` | YES |  |  | `` | `` |
| 57 | `RSV_40` | `char(35)` | YES |  |  | `` | `` |
| 58 | `RSV_41` | `char(35)` | YES |  |  | `` | `` |
| 59 | `RSV_42` | `char(35)` | YES |  |  | `` | `` |
| 60 | `RSV_43` | `char(35)` | YES |  |  | `` | `` |
| 61 | `RSV_44` | `char(35)` | YES |  |  | `` | `` |
| 62 | `RSV_45` | `char(35)` | YES |  |  | `` | `` |
| 63 | `RSV_46` | `char(35)` | YES |  |  | `` | `` |
| 64 | `RSV_47` | `char(35)` | YES |  |  | `` | `` |
| 65 | `RSV_48` | `char(35)` | YES |  |  | `` | `` |
| 66 | `RSV_49` | `char(35)` | YES |  |  | `` | `` |
| 67 | `RSV_50` | `char(35)` | YES |  |  | `` | `` |
| 68 | `RSV_51` | `char(35)` | YES |  |  | `` | `` |
| 69 | `RSV_52` | `char(35)` | YES |  |  | `` | `` |
| 70 | `RSV_53` | `char(35)` | YES |  |  | `` | `` |
| 71 | `RSV_54` | `char(35)` | YES |  |  | `` | `` |
| 72 | `RSV_55` | `char(35)` | YES |  |  | `` | `` |
| 73 | `RSV_56` | `char(35)` | YES |  |  | `` | `` |
| 74 | `RSV_57` | `char(35)` | YES |  |  | `` | `` |
| 75 | `RSV_58` | `char(35)` | YES |  |  | `` | `` |
| 76 | `RSV_59` | `char(35)` | YES |  |  | `` | `` |
| 77 | `RSV_60` | `char(35)` | YES |  |  | `` | `` |
| 78 | `RSV_61` | `char(35)` | YES |  |  | `` | `` |
| 79 | `RSV_62` | `char(35)` | YES |  |  | `` | `` |
| 80 | `RSV_63` | `char(35)` | YES |  |  | `` | `` |
| 81 | `RSV_64` | `char(35)` | YES |  |  | `` | `` |
| 82 | `RSV_65` | `char(35)` | YES |  |  | `` | `` |
| 83 | `RSV_66` | `char(35)` | YES |  |  | `` | `` |
| 84 | `RSV_67` | `char(35)` | YES |  |  | `` | `` |
| 85 | `RSV_68` | `char(35)` | YES |  |  | `` | `` |
| 86 | `RSV_69` | `char(35)` | YES |  |  | `` | `` |
| 87 | `RSV_70` | `char(35)` | YES |  |  | `` | `` |
| 88 | `RSV_71` | `char(35)` | YES |  |  | `` | `` |
| 89 | `RSV_72` | `char(35)` | YES |  |  | `` | `` |
| 90 | `RSV_73` | `char(35)` | YES |  |  | `` | `` |
| 91 | `RSV_74` | `char(35)` | YES |  |  | `` | `` |
| 92 | `RSV_75` | `char(35)` | YES |  |  | `` | `` |
| 93 | `RSV_76` | `char(35)` | YES |  |  | `` | `` |
| 94 | `RSV_77` | `char(35)` | YES |  |  | `` | `` |
| 95 | `RSV_78` | `char(35)` | YES |  |  | `` | `` |
| 96 | `RSV_79` | `char(35)` | YES |  |  | `` | `` |
| 97 | `RSV_80` | `char(35)` | YES |  |  | `` | `` |
| 98 | `RSV_81` | `char(35)` | YES |  |  | `` | `` |
| 99 | `RSV_82` | `char(35)` | YES |  |  | `` | `` |
| 100 | `RSV_83` | `char(35)` | YES |  |  | `` | `` |
| 101 | `RSV_84` | `char(35)` | YES |  |  | `` | `` |
| 102 | `RSV_85` | `char(35)` | YES |  |  | `` | `` |
| 103 | `RSV_86` | `char(35)` | YES |  |  | `` | `` |
| 104 | `RSV_87` | `char(35)` | YES |  |  | `` | `` |
| 105 | `RSV_88` | `char(35)` | YES |  |  | `` | `` |
| 106 | `RSV_89` | `char(35)` | YES |  |  | `` | `` |
| 107 | `RSV_90` | `char(35)` | YES |  |  | `` | `` |
| 108 | `RSV_91` | `char(35)` | YES |  |  | `` | `` |
| 109 | `RSV_92` | `char(35)` | YES |  |  | `` | `` |
| 110 | `RSV_93` | `char(35)` | YES |  |  | `` | `` |
| 111 | `RSV_94` | `char(35)` | YES |  |  | `` | `` |
| 112 | `RSV_95` | `char(35)` | YES |  |  | `` | `` |
| 113 | `RSV_96` | `char(35)` | YES |  |  | `` | `` |
| 114 | `RSV_97` | `char(35)` | YES |  |  | `` | `` |
| 115 | `RSV_98` | `char(35)` | YES |  |  | `` | `` |
| 116 | `RSV_99` | `char(35)` | YES |  |  | `` | `` |
| 117 | `RSV_100` | `char(35)` | YES |  |  | `` | `` |
| 118 | `RSV_101` | `char(35)` | YES |  |  | `` | `` |
| 119 | `RSV_102` | `char(35)` | YES |  |  | `` | `` |
| 120 | `RSV_103` | `char(35)` | YES |  |  | `` | `` |
| 121 | `RSV_104` | `char(35)` | YES |  |  | `` | `` |
| 122 | `RSV_105` | `char(35)` | YES |  |  | `` | `` |
| 123 | `RSV_106` | `char(35)` | YES |  |  | `` | `` |
| 124 | `RSV_107` | `char(35)` | YES |  |  | `` | `` |
| 125 | `RSV_108` | `char(35)` | YES |  |  | `` | `` |
| 126 | `RSV_109` | `char(35)` | YES |  |  | `` | `` |
| 127 | `RSV_110` | `char(35)` | YES |  |  | `` | `` |
| 128 | `RSV_112` | `char(35)` | YES |  |  | `` | `` |
| 129 | `RSV_113` | `char(35)` | YES |  |  | `` | `` |
| 130 | `RSV_114` | `char(35)` | YES |  |  | `` | `` |
| 131 | `RSV_115` | `char(35)` | YES |  |  | `` | `` |
| 132 | `RSV_116` | `char(35)` | YES |  |  | `` | `` |
| 133 | `RSV_117` | `char(35)` | YES |  |  | `` | `` |
| 134 | `RSV_118` | `char(35)` | YES |  |  | `` | `` |
| 135 | `RSV_119` | `char(35)` | YES |  |  | `` | `` |
| 136 | `RSV_120` | `char(35)` | YES |  |  | `` | `` |
| 137 | `RSV_121` | `char(35)` | YES |  |  | `` | `` |
| 138 | `RSV_122` | `char(35)` | YES |  |  | `` | `` |
| 139 | `RSV_123` | `char(35)` | YES |  |  | `` | `` |
| 140 | `RSV_124` | `char(35)` | YES |  |  | `` | `` |
| 141 | `RSV_125` | `char(35)` | YES |  |  | `` | `` |
| 142 | `RSV_126` | `char(35)` | YES |  |  | `` | `` |
| 143 | `RSV_127` | `char(35)` | YES |  |  | `` | `` |
| 144 | `RSV_128` | `char(35)` | YES |  |  | `` | `` |
| 145 | `RSV_129` | `char(35)` | YES |  |  | `` | `` |
| 146 | `RSV_130` | `char(35)` | YES |  |  | `` | `` |
| 147 | `RSV_131` | `char(35)` | YES |  |  | `` | `` |
| 148 | `RSV_132` | `char(35)` | YES |  |  | `` | `` |
| 149 | `RSV_133` | `char(35)` | YES |  |  | `` | `` |
| 150 | `RSV_134` | `char(35)` | YES |  |  | `` | `` |
| 151 | `RSV_135` | `char(35)` | YES |  |  | `` | `` |
| 152 | `RSV_136` | `char(35)` | YES |  |  | `` | `` |
| 153 | `RSV_137` | `char(35)` | YES |  |  | `` | `` |
| 154 | `RSV_138` | `char(35)` | YES |  |  | `` | `` |
| 155 | `RSV_139` | `char(35)` | YES |  |  | `` | `` |
| 156 | `RSV_140` | `char(35)` | YES |  |  | `` | `` |
| 157 | `RSV_141` | `char(35)` | YES |  |  | `` | `` |
| 158 | `RSV_142` | `char(35)` | YES |  |  | `` | `` |
| 159 | `RSV_143` | `char(35)` | YES |  |  | `` | `` |
| 160 | `RSV_144` | `char(35)` | YES |  |  | `` | `` |
| 161 | `RSV_145` | `char(35)` | YES |  |  | `` | `` |
| 162 | `RSV_146` | `char(35)` | YES |  |  | `` | `` |
| 163 | `RSV_147` | `char(35)` | YES |  |  | `` | `` |
| 164 | `RSV_148` | `char(35)` | YES |  |  | `` | `` |
| 165 | `RSV_149` | `char(35)` | YES |  |  | `` | `` |
| 166 | `RSV_150` | `char(35)` | YES |  |  | `` | `` |
| 167 | `RSV_151` | `char(35)` | YES |  |  | `` | `` |
| 168 | `RSV_152` | `char(35)` | YES |  |  | `` | `` |
| 169 | `RSV_153` | `char(35)` | YES |  |  | `` | `` |
| 170 | `RSV_154` | `char(35)` | YES |  |  | `` | `` |
| 171 | `RSV_155` | `char(35)` | YES |  |  | `` | `` |
| 172 | `RSV_156` | `char(35)` | YES |  |  | `` | `` |
| 173 | `RSV_157` | `char(35)` | YES |  |  | `` | `` |
| 174 | `RSV_158` | `char(35)` | YES |  |  | `` | `` |
| 175 | `RSV_159` | `char(35)` | YES |  |  | `` | `` |
| 176 | `RSV_160` | `char(35)` | YES |  |  | `` | `` |
| 177 | `RSV_161` | `char(35)` | YES |  |  | `` | `` |
| 178 | `RSV_162` | `char(35)` | YES |  |  | `` | `` |
| 179 | `RSV_163` | `char(35)` | YES |  |  | `` | `` |
| 180 | `RSV_164` | `char(35)` | YES |  |  | `` | `` |
| 181 | `RSV_165` | `char(35)` | YES |  |  | `` | `` |
| 182 | `RSV_166` | `char(35)` | YES |  |  | `` | `` |
| 183 | `RSV_167` | `char(35)` | YES |  |  | `` | `` |
| 184 | `RSV_168` | `char(35)` | YES |  |  | `` | `` |
| 185 | `RSV_169` | `char(35)` | YES |  |  | `` | `` |
| 186 | `RSV_170` | `char(35)` | YES |  |  | `` | `` |
| 187 | `RSV_171` | `char(35)` | YES |  |  | `` | `` |
| 188 | `RSV_172` | `char(35)` | YES |  |  | `` | `` |
| 189 | `RSV_173` | `char(35)` | YES |  |  | `` | `` |
| 190 | `RSV_174` | `char(35)` | YES |  |  | `` | `` |
| 191 | `RSV_175` | `char(35)` | YES |  |  | `` | `` |
| 192 | `RSV_176` | `char(35)` | YES |  |  | `` | `` |
| 193 | `RSV_177` | `char(35)` | YES |  |  | `` | `` |
| 194 | `RSV_178` | `char(35)` | YES |  |  | `` | `` |
| 195 | `RSV_179` | `char(35)` | YES |  |  | `` | `` |
| 196 | `RSV_180` | `char(35)` | YES |  |  | `` | `` |
| 197 | `RSV_181` | `char(35)` | YES |  |  | `` | `` |
| 198 | `RSV_182` | `char(35)` | YES |  |  | `` | `` |
| 199 | `RSV_183` | `char(35)` | YES |  |  | `` | `` |
| 200 | `RSV_184` | `char(35)` | YES |  |  | `` | `` |
| 201 | `RSV_185` | `char(35)` | YES |  |  | `` | `` |
| 202 | `RSV_186` | `char(35)` | YES |  |  | `` | `` |
| 203 | `RSV_187` | `char(35)` | YES |  |  | `` | `` |
| 204 | `RSV_188` | `char(35)` | YES |  |  | `` | `` |
| 205 | `RSV_189` | `char(35)` | YES |  |  | `` | `` |
| 206 | `RSV_190` | `char(35)` | YES |  |  | `` | `` |
| 207 | `RSV_191` | `char(35)` | YES |  |  | `` | `` |
| 208 | `RSV_192` | `char(35)` | YES |  |  | `` | `` |
| 209 | `RSV_193` | `char(35)` | YES |  |  | `` | `` |
| 210 | `RSV_194` | `char(35)` | YES |  |  | `` | `` |
| 211 | `RSV_195` | `char(35)` | YES |  |  | `` | `` |
| 212 | `RSV_196` | `char(35)` | YES |  |  | `` | `` |
| 213 | `RSV_197` | `char(35)` | YES |  |  | `` | `` |
| 214 | `RSV_198` | `char(35)` | YES |  |  | `` | `` |
| 215 | `RSV_199` | `char(35)` | YES |  |  | `` | `` |
| 216 | `RSV_200` | `char(35)` | YES |  |  | `` | `` |

## 12. `[dbo].[omsphead]`

- Rows: `179087`
- Columns: `74`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `SHIPTONAME` | `char(50)` | YES |  |  | `` | `` |
| 2 | `SHIPTOADDR1` | `char(50)` | YES |  |  | `` | `` |
| 3 | `SHIPTOADDR2` | `char(50)` | YES |  |  | `` | `` |
| 4 | `SHIPTOADDR3` | `char(50)` | YES |  |  | `` | `` |
| 5 | `SHIPTOCITY` | `char(30)` | YES |  |  | `` | `` |
| 6 | `SHIPTOSTATE` | `char(10)` | YES |  |  | `` | `` |
| 7 | `SHIPTOZIPCD` | `char(10)` | YES |  |  | `` | `` |
| 8 | `SHIPTOCOUNTRY` | `char(30)` | YES |  |  | `` | `` |
| 9 | `SHIPTOPHONE` | `char(20)` | YES |  |  | `` | `` |
| 10 | `SHIPTOFAX` | `char(20)` | YES |  |  | `` | `` |
| 11 | `SHIPTOEMAIL` | `char(60)` | YES |  |  | `` | `` |
| 12 | `SHIPTOATTN` | `char(35)` | YES |  |  | `` | `` |
| 13 | `SHIPREFER` | `char(60)` | YES |  |  | `` | `` |
| 14 | `UPSSERVICE` | `char(20)` | YES |  |  | `` | `` |
| 15 | `FDXSERVICE` | `char(20)` | YES |  |  | `` | `` |
| 16 | `OTHERSERVICE` | `char(20)` | YES |  |  | `` | `` |
| 17 | `BILLINGTYPE` | `char(20)` | YES |  |  | `` | `` |
| 18 | `SHIPPACKAGE` | `char(10)` | YES |  |  | `` | `` |
| 19 | `CUST_PO_NUM` | `char(35)` | YES |  |  | `` | `` |
| 20 | `INVOICE` | `char(20)` | NO |  |  | `` | `` |
| 21 | `INVOICETYPE` | `char(4)` | NO |  |  | `` | `` |
| 22 | `SHIPNOTIFY` | `char(1)` | YES |  |  | `` | `` |
| 23 | `NOTIFYTYPE` | `char(1)` | YES |  |  | `` | `` |
| 24 | `SHIPDATE` | `datetime` | YES |  |  | `` | `` |
| 25 | `SHIPTYPE` | `int` | YES |  |  | `` | `` |
| 26 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 27 | `INVS_TM` | `int` | YES |  |  | `` | `` |
| 28 | `CUS_ID` | `char(20)` | YES |  |  | `` | `` |
| 29 | `SHIPLINE` | `int` | YES |  |  | `` | `` |
| 30 | `SHIPDESC1` | `char(60)` | YES |  |  | `` | `` |
| 31 | `SHIPDESC2` | `char(60)` | YES |  |  | `` | `` |
| 32 | `SHIPDESC3` | `char(60)` | YES |  |  | `` | `` |
| 33 | `SHIPFIELD1` | `int` | YES |  |  | `` | `` |
| 34 | `SHIPFIELD2` | `int` | YES |  |  | `` | `` |
| 35 | `THIRDPARTY` | `char(1)` | YES |  |  | `` | `` |
| 36 | `THIRDACCT` | `char(20)` | YES |  |  | `` | `` |
| 37 | `INVOICEAMT` | `decimal(17,2)` | YES |  |  | `` | `` |
| 38 | `SHIPPINGFEE1` | `decimal(17,2)` | YES |  |  | `` | `` |
| 39 | `HANDLINGFEE` | `decimal(17,2)` | YES |  |  | `` | `` |
| 40 | `TAXAMT` | `decimal(17,2)` | YES |  |  | `` | `` |
| 41 | `SHIPPINGFEE2` | `decimal(17,2)` | YES |  |  | `` | `` |
| 42 | `CODAMOUNT` | `decimal(17,2)` | YES |  |  | `` | `` |
| 43 | `INSURANCEAMT` | `decimal(17,2)` | YES |  |  | `` | `` |
| 44 | `SHIPFMNAME` | `char(50)` | YES |  |  | `` | `` |
| 45 | `SHIPFMATTN` | `char(50)` | YES |  |  | `` | `` |
| 46 | `SHIPFMADDR1` | `char(50)` | YES |  |  | `` | `` |
| 47 | `SHIPFMADDR2` | `char(50)` | YES |  |  | `` | `` |
| 48 | `SHIPFMADDR3` | `char(50)` | YES |  |  | `` | `` |
| 49 | `SHIPFMCOUNTRY` | `char(40)` | YES |  |  | `` | `` |
| 50 | `SHIPFMZIPCD` | `char(20)` | YES |  |  | `` | `` |
| 51 | `SHIPFMCITY` | `char(40)` | YES |  |  | `` | `` |
| 52 | `SHIPFMSTATE` | `char(40)` | YES |  |  | `` | `` |
| 53 | `SHIPFMPHONE` | `char(20)` | YES |  |  | `` | `` |
| 54 | `SHIPFMFAX` | `char(20)` | YES |  |  | `` | `` |
| 55 | `SHIPFMTAXID` | `char(20)` | YES |  |  | `` | `` |
| 56 | `SHIPFMTAXIDTYPE` | `char(20)` | YES |  |  | `` | `` |
| 57 | `SHIPFMUPSACCT` | `char(20)` | YES |  |  | `` | `` |
| 58 | `SHIPFMRESIND` | `char(20)` | YES |  |  | `` | `` |
| 59 | `THIRDNAME` | `char(50)` | YES |  |  | `` | `` |
| 60 | `THIRDATTN` | `char(50)` | YES |  |  | `` | `` |
| 61 | `THIRDADDR1` | `char(50)` | YES |  |  | `` | `` |
| 62 | `THIRDADDR2` | `char(50)` | YES |  |  | `` | `` |
| 63 | `THIRDADDR3` | `char(50)` | YES |  |  | `` | `` |
| 64 | `THIRDCOUNTRY` | `char(40)` | YES |  |  | `` | `` |
| 65 | `THIRDZIPCD` | `char(20)` | YES |  |  | `` | `` |
| 66 | `THIRDCITY` | `char(40)` | YES |  |  | `` | `` |
| 67 | `THIRDSTATE` | `char(40)` | YES |  |  | `` | `` |
| 68 | `THIRDPHONE` | `char(20)` | YES |  |  | `` | `` |
| 69 | `THIRDFAX` | `char(20)` | YES |  |  | `` | `` |
| 70 | `THIRDUPSACCT` | `char(20)` | YES |  |  | `` | `` |
| 71 | `ESTWEIGHT` | `decimal(17,2)` | YES |  |  | `` | `` |
| 72 | `CODTYPE` | `char(1)` | YES |  |  | `` | `` |
| 73 | `HUNDREDWEIGHT` | `char(1)` | YES |  |  | `` | `` |
| 74 | `REFERENCENO` | `char(40)` | YES |  |  | `` | `` |

## 13. `[dbo].[bin_pur]`

- Rows: `108183`
- Columns: `14`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PUR_NUM` | `char(8)` | NO |  |  | `` | `` |
| 2 | `PUR_CD` | `tinyint` | NO |  |  | `` | `` |
| 3 | `BATCH_NUM` | `int` | NO |  |  | `` | `` |
| 4 | `NT_NUM` | `smallint` | NO |  |  | `` | `` |
| 5 | `PROD_CD` | `char(20)` | NO |  |  | `` | `` |
| 6 | `WHS_NUM` | `char(8)` | NO |  |  | `` | `` |
| 7 | `BIN_CD` | `char(16)` | NO |  |  | `` | `` |
| 8 | `PO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `RCVD_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `CAN_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `RTN_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `COMM_LN` | `int` | YES |  |  | `` | `` |
| 13 | `PRICE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `COST` | `decimal(21,6)` | YES |  |  | `` | `` |

## 14. `[dbo].[plog]`

- Rows: `107404`
- Columns: `54`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `LOG_DATE` | `int` | YES |  |  | `` | `` |
| 2 | `LOG_TIME` | `int` | YES |  |  | `` | `` |
| 3 | `VEN_ID` | `char(11)` | YES |  |  | `` | `` |
| 4 | `INVS_NUM` | `char(10)` | YES |  |  | `` | `` |
| 5 | `PUR_NUM` | `char(8)` | NO |  |  | `` | `` |
| 6 | `PUR_CD` | `int` | NO |  |  | `` | `` |
| 7 | `PROD_CD` | `char(21)` | YES |  |  | `` | `` |
| 8 | `LOG_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `BASE_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `HDL_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `SHP_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `TAX_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `CAN_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `EST_DT` | `int` | YES |  |  | `` | `` |
| 15 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `PUR_LNT` | `char(1)` | YES |  |  | `` | `` |
| 17 | `NT_NUM` | `int` | YES |  |  | `` | `` |
| 18 | `COMM_LN` | `smallint` | NO |  |  | `` | `` |
| 19 | `UT_DESC` | `char(60)` | YES |  |  | `` | `` |
| 20 | `PROD_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `WT_QTY` | `int` | YES |  |  | `` | `` |
| 22 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 23 | `BATCH_NUM` | `int` | NO |  |  | `` | `` |
| 24 | `CAL_SEL` | `tinyint` | YES |  |  | `` | `` |
| 25 | `UT_SHP` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `UT_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `EXCH_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `PC_UNIT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `DEF_UT` | `char(2)` | YES |  |  | `` | `` |
| 30 | `CLASS_ITEM` | `char(20)` | YES |  |  | `` | `` |
| 31 | `SO_NUM` | `char(12)` | YES |  |  | `` | `` |
| 32 | `SO_DT` | `int` | YES |  |  | `` | `` |
| 33 | `TYPE_CD` | `char(6)` | YES |  |  | `` | `` |
| 34 | `SO_NT_NUM` | `int` | YES |  |  | `` | `` |
| 35 | `CURRENCY` | `char(4)` | YES |  |  | `` | `` |
| 36 | `EXC_RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `CURRENCY_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `DIV_CD` | `char(10)` | YES |  |  | `` | `` |
| 39 | `PRJ_CD` | `char(10)` | YES |  |  | `` | `` |
| 40 | `JOB_CD` | `char(10)` | YES |  |  | `` | `` |
| 41 | `FINAL_CUS` | `char(30)` | YES |  |  | `` | `` |
| 42 | `LOT_NUM` | `char(20)` | YES |  |  | `` | `` |
| 43 | `ALLOC_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 44 | `UT_MISC` | `decimal(21,6)` | YES |  |  | `` | `` |
| 45 | `ITMSHP_DT` | `int` | YES |  |  | `` | `` |
| 46 | `CFMSHP_DT` | `int` | YES |  |  | `` | `` |
| 47 | `AVG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 48 | `INV_MK` | `char(20)` | YES |  |  | `` | `` |
| 49 | `INV_PCK` | `char(20)` | YES |  |  | `` | `` |
| 50 | `INV_MFR` | `char(20)` | YES |  |  | `` | `` |
| 51 | `ERR_CODE` | `char(20)` | YES |  |  | `` | `` |
| 52 | `PROD_DT` | `int` | YES |  |  | `` | `` |
| 53 | `ESTSHP_DT` | `int` | YES |  |  | `` | `` |
| 54 | `Id` | `int` | NO | YES | YES | `` | `` |

## 15. `[dbo].[order2e]`

- Rows: `91674`
- Columns: `216`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ORD_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `PO_NUM` | `varchar(22)` | YES |  |  | `` | `` |
| 3 | `PO_DT` | `int` | YES |  |  | `` | `` |
| 4 | `PURPOSE` | `varchar(2)` | YES |  |  | `` | `` |
| 5 | `PO_TYPE` | `varchar(2)` | YES |  |  | `` | `` |
| 6 | `BATCH_NUM` | `varchar(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_NUM` | `varchar(30)` | YES |  |  | `` | `` |
| 8 | `VEN_ID` | `varchar(20)` | YES |  |  | `` | `` |
| 9 | `SHP_DC_NUM` | `varchar(20)` | YES |  |  | `` | `` |
| 10 | `SLD_CUS_ID` | `varchar(20)` | YES |  |  | `` | `` |
| 11 | `INTERNAL_PO` | `varchar(20)` | YES |  |  | `` | `` |
| 12 | `OUR_TERM_CD` | `varchar(5)` | YES |  |  | `` | `` |
| 13 | `DISC_PER` | `varchar(8)` | YES |  |  | `` | `` |
| 14 | `DISC_DUE_DT` | `varchar(8)` | YES |  |  | `` | `` |
| 15 | `DISC_DAYS_DUE` | `varchar(4)` | YES |  |  | `` | `` |
| 16 | `NET_DUE_DT` | `varchar(8)` | YES |  |  | `` | `` |
| 17 | `NET_DAYS_DUE` | `varchar(4)` | YES |  |  | `` | `` |
| 18 | `RSV_1` | `varchar(35)` | YES |  |  | `` | `` |
| 19 | `RSV_2` | `varchar(35)` | YES |  |  | `` | `` |
| 20 | `RSV_3` | `varchar(35)` | YES |  |  | `` | `` |
| 21 | `RSV_4` | `varchar(35)` | YES |  |  | `` | `` |
| 22 | `RSV_5` | `varchar(35)` | YES |  |  | `` | `` |
| 23 | `RSV_6` | `varchar(35)` | YES |  |  | `` | `` |
| 24 | `RSV_7` | `varchar(35)` | YES |  |  | `` | `` |
| 25 | `RSV_8` | `varchar(35)` | YES |  |  | `` | `` |
| 26 | `RSV_9` | `varchar(35)` | YES |  |  | `` | `` |
| 27 | `RSV_10` | `varchar(35)` | YES |  |  | `` | `` |
| 28 | `RSV_11` | `varchar(35)` | YES |  |  | `` | `` |
| 29 | `RSV_12` | `varchar(35)` | YES |  |  | `` | `` |
| 30 | `RSV_13` | `varchar(35)` | YES |  |  | `` | `` |
| 31 | `RSV_14` | `varchar(35)` | YES |  |  | `` | `` |
| 32 | `RSV_15` | `varchar(35)` | YES |  |  | `` | `` |
| 33 | `RSV_16` | `varchar(35)` | YES |  |  | `` | `` |
| 34 | `RSV_17` | `varchar(35)` | YES |  |  | `` | `` |
| 35 | `RSV_18` | `varchar(35)` | YES |  |  | `` | `` |
| 36 | `RSV_19` | `varchar(35)` | YES |  |  | `` | `` |
| 37 | `RSV_20` | `varchar(35)` | YES |  |  | `` | `` |
| 38 | `RSV_21` | `varchar(35)` | YES |  |  | `` | `` |
| 39 | `RSV_22` | `varchar(35)` | YES |  |  | `` | `` |
| 40 | `RSV_23` | `varchar(35)` | YES |  |  | `` | `` |
| 41 | `RSV_24` | `varchar(35)` | YES |  |  | `` | `` |
| 42 | `RSV_25` | `varchar(35)` | YES |  |  | `` | `` |
| 43 | `RSV_26` | `varchar(35)` | YES |  |  | `` | `` |
| 44 | `RSV_27` | `varchar(35)` | YES |  |  | `` | `` |
| 45 | `RSV_28` | `varchar(35)` | YES |  |  | `` | `` |
| 46 | `RSV_29` | `varchar(35)` | YES |  |  | `` | `` |
| 47 | `RSV_30` | `varchar(35)` | YES |  |  | `` | `` |
| 48 | `RSV_31` | `varchar(35)` | YES |  |  | `` | `` |
| 49 | `RSV_32` | `varchar(35)` | YES |  |  | `` | `` |
| 50 | `RSV_33` | `varchar(35)` | YES |  |  | `` | `` |
| 51 | `RSV_34` | `varchar(35)` | YES |  |  | `` | `` |
| 52 | `RSV_35` | `varchar(35)` | YES |  |  | `` | `` |
| 53 | `RSV_36` | `varchar(35)` | YES |  |  | `` | `` |
| 54 | `RSV_37` | `varchar(35)` | YES |  |  | `` | `` |
| 55 | `RSV_38` | `varchar(35)` | YES |  |  | `` | `` |
| 56 | `RSV_39` | `varchar(35)` | YES |  |  | `` | `` |
| 57 | `RSV_40` | `varchar(35)` | YES |  |  | `` | `` |
| 58 | `RSV_41` | `varchar(35)` | YES |  |  | `` | `` |
| 59 | `RSV_42` | `varchar(35)` | YES |  |  | `` | `` |
| 60 | `RSV_43` | `varchar(35)` | YES |  |  | `` | `` |
| 61 | `RSV_44` | `varchar(35)` | YES |  |  | `` | `` |
| 62 | `RSV_45` | `varchar(35)` | YES |  |  | `` | `` |
| 63 | `RSV_46` | `varchar(35)` | YES |  |  | `` | `` |
| 64 | `RSV_47` | `varchar(35)` | YES |  |  | `` | `` |
| 65 | `RSV_48` | `varchar(35)` | YES |  |  | `` | `` |
| 66 | `RSV_49` | `varchar(35)` | YES |  |  | `` | `` |
| 67 | `RSV_50` | `varchar(35)` | YES |  |  | `` | `` |
| 68 | `RSV_51` | `varchar(35)` | YES |  |  | `` | `` |
| 69 | `RSV_52` | `varchar(35)` | YES |  |  | `` | `` |
| 70 | `RSV_53` | `varchar(35)` | YES |  |  | `` | `` |
| 71 | `RSV_54` | `varchar(35)` | YES |  |  | `` | `` |
| 72 | `RSV_55` | `varchar(35)` | YES |  |  | `` | `` |
| 73 | `RSV_56` | `varchar(35)` | YES |  |  | `` | `` |
| 74 | `RSV_57` | `varchar(35)` | YES |  |  | `` | `` |
| 75 | `RSV_58` | `varchar(35)` | YES |  |  | `` | `` |
| 76 | `RSV_59` | `varchar(35)` | YES |  |  | `` | `` |
| 77 | `RSV_60` | `varchar(35)` | YES |  |  | `` | `` |
| 78 | `RSV_61` | `varchar(35)` | YES |  |  | `` | `` |
| 79 | `RSV_62` | `varchar(35)` | YES |  |  | `` | `` |
| 80 | `RSV_63` | `varchar(35)` | YES |  |  | `` | `` |
| 81 | `RSV_64` | `varchar(35)` | YES |  |  | `` | `` |
| 82 | `RSV_65` | `varchar(35)` | YES |  |  | `` | `` |
| 83 | `RSV_66` | `varchar(35)` | YES |  |  | `` | `` |
| 84 | `RSV_67` | `varchar(35)` | YES |  |  | `` | `` |
| 85 | `RSV_68` | `varchar(35)` | YES |  |  | `` | `` |
| 86 | `RSV_69` | `varchar(35)` | YES |  |  | `` | `` |
| 87 | `RSV_70` | `varchar(35)` | YES |  |  | `` | `` |
| 88 | `RSV_71` | `varchar(35)` | YES |  |  | `` | `` |
| 89 | `RSV_72` | `varchar(35)` | YES |  |  | `` | `` |
| 90 | `RSV_73` | `varchar(35)` | YES |  |  | `` | `` |
| 91 | `RSV_74` | `varchar(35)` | YES |  |  | `` | `` |
| 92 | `RSV_75` | `varchar(35)` | YES |  |  | `` | `` |
| 93 | `RSV_76` | `varchar(35)` | YES |  |  | `` | `` |
| 94 | `RSV_77` | `varchar(35)` | YES |  |  | `` | `` |
| 95 | `RSV_78` | `varchar(35)` | YES |  |  | `` | `` |
| 96 | `RSV_79` | `varchar(35)` | YES |  |  | `` | `` |
| 97 | `RSV_80` | `varchar(35)` | YES |  |  | `` | `` |
| 98 | `RSV_81` | `varchar(35)` | YES |  |  | `` | `` |
| 99 | `RSV_82` | `varchar(35)` | YES |  |  | `` | `` |
| 100 | `RSV_83` | `varchar(35)` | YES |  |  | `` | `` |
| 101 | `RSV_84` | `varchar(35)` | YES |  |  | `` | `` |
| 102 | `RSV_85` | `varchar(35)` | YES |  |  | `` | `` |
| 103 | `RSV_86` | `varchar(35)` | YES |  |  | `` | `` |
| 104 | `RSV_87` | `varchar(35)` | YES |  |  | `` | `` |
| 105 | `RSV_88` | `varchar(35)` | YES |  |  | `` | `` |
| 106 | `RSV_89` | `varchar(35)` | YES |  |  | `` | `` |
| 107 | `RSV_90` | `varchar(35)` | YES |  |  | `` | `` |
| 108 | `RSV_91` | `varchar(35)` | YES |  |  | `` | `` |
| 109 | `RSV_92` | `varchar(35)` | YES |  |  | `` | `` |
| 110 | `RSV_93` | `varchar(35)` | YES |  |  | `` | `` |
| 111 | `RSV_94` | `varchar(35)` | YES |  |  | `` | `` |
| 112 | `RSV_95` | `varchar(35)` | YES |  |  | `` | `` |
| 113 | `RSV_96` | `varchar(35)` | YES |  |  | `` | `` |
| 114 | `RSV_97` | `varchar(35)` | YES |  |  | `` | `` |
| 115 | `RSV_98` | `varchar(35)` | YES |  |  | `` | `` |
| 116 | `RSV_99` | `varchar(35)` | YES |  |  | `` | `` |
| 117 | `RSV_100` | `varchar(35)` | YES |  |  | `` | `` |
| 118 | `RSV_101` | `varchar(35)` | YES |  |  | `` | `` |
| 119 | `RSV_102` | `varchar(35)` | YES |  |  | `` | `` |
| 120 | `RSV_103` | `varchar(35)` | YES |  |  | `` | `` |
| 121 | `RSV_104` | `varchar(35)` | YES |  |  | `` | `` |
| 122 | `RSV_105` | `varchar(35)` | YES |  |  | `` | `` |
| 123 | `RSV_106` | `varchar(35)` | YES |  |  | `` | `` |
| 124 | `RSV_107` | `varchar(35)` | YES |  |  | `` | `` |
| 125 | `RSV_108` | `varchar(35)` | YES |  |  | `` | `` |
| 126 | `RSV_109` | `varchar(35)` | YES |  |  | `` | `` |
| 127 | `RSV_110` | `varchar(35)` | YES |  |  | `` | `` |
| 128 | `RSV_112` | `varchar(35)` | YES |  |  | `` | `` |
| 129 | `RSV_113` | `varchar(35)` | YES |  |  | `` | `` |
| 130 | `RSV_114` | `varchar(35)` | YES |  |  | `` | `` |
| 131 | `RSV_115` | `varchar(35)` | YES |  |  | `` | `` |
| 132 | `RSV_116` | `varchar(35)` | YES |  |  | `` | `` |
| 133 | `RSV_117` | `varchar(35)` | YES |  |  | `` | `` |
| 134 | `RSV_118` | `varchar(35)` | YES |  |  | `` | `` |
| 135 | `RSV_119` | `varchar(35)` | YES |  |  | `` | `` |
| 136 | `RSV_120` | `varchar(35)` | YES |  |  | `` | `` |
| 137 | `RSV_121` | `varchar(35)` | YES |  |  | `` | `` |
| 138 | `RSV_122` | `varchar(35)` | YES |  |  | `` | `` |
| 139 | `RSV_123` | `varchar(35)` | YES |  |  | `` | `` |
| 140 | `RSV_124` | `varchar(35)` | YES |  |  | `` | `` |
| 141 | `RSV_125` | `varchar(35)` | YES |  |  | `` | `` |
| 142 | `RSV_126` | `varchar(35)` | YES |  |  | `` | `` |
| 143 | `RSV_127` | `varchar(35)` | YES |  |  | `` | `` |
| 144 | `RSV_128` | `varchar(35)` | YES |  |  | `` | `` |
| 145 | `RSV_129` | `varchar(35)` | YES |  |  | `` | `` |
| 146 | `RSV_130` | `varchar(35)` | YES |  |  | `` | `` |
| 147 | `RSV_131` | `varchar(35)` | YES |  |  | `` | `` |
| 148 | `RSV_132` | `varchar(35)` | YES |  |  | `` | `` |
| 149 | `RSV_133` | `varchar(35)` | YES |  |  | `` | `` |
| 150 | `RSV_134` | `varchar(35)` | YES |  |  | `` | `` |
| 151 | `RSV_135` | `varchar(35)` | YES |  |  | `` | `` |
| 152 | `RSV_136` | `varchar(35)` | YES |  |  | `` | `` |
| 153 | `RSV_137` | `varchar(35)` | YES |  |  | `` | `` |
| 154 | `RSV_138` | `varchar(35)` | YES |  |  | `` | `` |
| 155 | `RSV_139` | `varchar(35)` | YES |  |  | `` | `` |
| 156 | `RSV_140` | `varchar(35)` | YES |  |  | `` | `` |
| 157 | `RSV_141` | `varchar(35)` | YES |  |  | `` | `` |
| 158 | `RSV_142` | `varchar(35)` | YES |  |  | `` | `` |
| 159 | `RSV_143` | `varchar(35)` | YES |  |  | `` | `` |
| 160 | `RSV_144` | `varchar(35)` | YES |  |  | `` | `` |
| 161 | `RSV_145` | `varchar(35)` | YES |  |  | `` | `` |
| 162 | `RSV_146` | `varchar(35)` | YES |  |  | `` | `` |
| 163 | `RSV_147` | `varchar(35)` | YES |  |  | `` | `` |
| 164 | `RSV_148` | `varchar(35)` | YES |  |  | `` | `` |
| 165 | `RSV_149` | `varchar(35)` | YES |  |  | `` | `` |
| 166 | `RSV_150` | `varchar(35)` | YES |  |  | `` | `` |
| 167 | `RSV_151` | `varchar(35)` | YES |  |  | `` | `` |
| 168 | `RSV_152` | `varchar(35)` | YES |  |  | `` | `` |
| 169 | `RSV_153` | `varchar(35)` | YES |  |  | `` | `` |
| 170 | `RSV_154` | `varchar(35)` | YES |  |  | `` | `` |
| 171 | `RSV_155` | `varchar(35)` | YES |  |  | `` | `` |
| 172 | `RSV_156` | `varchar(35)` | YES |  |  | `` | `` |
| 173 | `RSV_157` | `varchar(35)` | YES |  |  | `` | `` |
| 174 | `RSV_158` | `varchar(35)` | YES |  |  | `` | `` |
| 175 | `RSV_159` | `varchar(35)` | YES |  |  | `` | `` |
| 176 | `RSV_160` | `varchar(35)` | YES |  |  | `` | `` |
| 177 | `RSV_161` | `varchar(35)` | YES |  |  | `` | `` |
| 178 | `RSV_162` | `varchar(35)` | YES |  |  | `` | `` |
| 179 | `RSV_163` | `varchar(35)` | YES |  |  | `` | `` |
| 180 | `RSV_164` | `varchar(35)` | YES |  |  | `` | `` |
| 181 | `RSV_165` | `varchar(35)` | YES |  |  | `` | `` |
| 182 | `RSV_166` | `varchar(35)` | YES |  |  | `` | `` |
| 183 | `RSV_167` | `varchar(35)` | YES |  |  | `` | `` |
| 184 | `RSV_168` | `varchar(35)` | YES |  |  | `` | `` |
| 185 | `RSV_169` | `varchar(35)` | YES |  |  | `` | `` |
| 186 | `RSV_170` | `varchar(35)` | YES |  |  | `` | `` |
| 187 | `RSV_171` | `varchar(35)` | YES |  |  | `` | `` |
| 188 | `RSV_172` | `varchar(35)` | YES |  |  | `` | `` |
| 189 | `RSV_173` | `varchar(35)` | YES |  |  | `` | `` |
| 190 | `RSV_174` | `varchar(35)` | YES |  |  | `` | `` |
| 191 | `RSV_175` | `varchar(35)` | YES |  |  | `` | `` |
| 192 | `RSV_176` | `varchar(35)` | YES |  |  | `` | `` |
| 193 | `RSV_177` | `varchar(35)` | YES |  |  | `` | `` |
| 194 | `RSV_178` | `varchar(35)` | YES |  |  | `` | `` |
| 195 | `RSV_179` | `varchar(35)` | YES |  |  | `` | `` |
| 196 | `RSV_180` | `varchar(35)` | YES |  |  | `` | `` |
| 197 | `RSV_181` | `varchar(35)` | YES |  |  | `` | `` |
| 198 | `RSV_182` | `varchar(35)` | YES |  |  | `` | `` |
| 199 | `RSV_183` | `varchar(35)` | YES |  |  | `` | `` |
| 200 | `RSV_184` | `varchar(35)` | YES |  |  | `` | `` |
| 201 | `RSV_185` | `varchar(35)` | YES |  |  | `` | `` |
| 202 | `RSV_186` | `varchar(35)` | YES |  |  | `` | `` |
| 203 | `RSV_187` | `varchar(35)` | YES |  |  | `` | `` |
| 204 | `RSV_188` | `varchar(35)` | YES |  |  | `` | `` |
| 205 | `RSV_189` | `varchar(35)` | YES |  |  | `` | `` |
| 206 | `RSV_190` | `varchar(35)` | YES |  |  | `` | `` |
| 207 | `RSV_191` | `varchar(35)` | YES |  |  | `` | `` |
| 208 | `RSV_192` | `varchar(35)` | YES |  |  | `` | `` |
| 209 | `RSV_193` | `varchar(35)` | YES |  |  | `` | `` |
| 210 | `RSV_194` | `varchar(35)` | YES |  |  | `` | `` |
| 211 | `RSV_195` | `varchar(35)` | YES |  |  | `` | `` |
| 212 | `RSV_196` | `varchar(35)` | YES |  |  | `` | `` |
| 213 | `RSV_197` | `varchar(35)` | YES |  |  | `` | `` |
| 214 | `RSV_198` | `varchar(35)` | YES |  |  | `` | `` |
| 215 | `RSV_199` | `varchar(35)` | YES |  |  | `` | `` |
| 216 | `RSV_200` | `varchar(35)` | YES |  |  | `` | `` |

## 16. `[dbo].[proddesc]`

- Rows: `89684`
- Columns: `32`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(20)` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `decimal(5,0)` | YES |  |  | `` | `` |
| 3 | `UT_DESC1` | `char(60)` | YES |  |  | `` | `` |
| 4 | `UT_DESC2` | `char(60)` | YES |  |  | `` | `` |
| 5 | `UT_DESC3` | `char(60)` | YES |  |  | `` | `` |
| 6 | `UT_DESC4` | `char(60)` | YES |  |  | `` | `` |
| 7 | `UT_DESC5` | `char(60)` | YES |  |  | `` | `` |
| 8 | `UT_DESC6` | `char(60)` | YES |  |  | `` | `` |
| 9 | `UT_DESC7` | `char(60)` | YES |  |  | `` | `` |
| 10 | `UT_DESC8` | `char(60)` | YES |  |  | `` | `` |
| 11 | `UT_DESC9` | `char(60)` | YES |  |  | `` | `` |
| 12 | `UT_DESC10` | `char(60)` | YES |  |  | `` | `` |
| 13 | `UT_DESC11` | `char(60)` | YES |  |  | `` | `` |
| 14 | `UT_DESC12` | `char(60)` | YES |  |  | `` | `` |
| 15 | `UT_DESC13` | `char(60)` | YES |  |  | `` | `` |
| 16 | `UT_DESC14` | `char(60)` | YES |  |  | `` | `` |
| 17 | `UT_DESC15` | `char(60)` | YES |  |  | `` | `` |
| 18 | `UT_DESC16` | `char(60)` | YES |  |  | `` | `` |
| 19 | `UT_DESC17` | `char(60)` | YES |  |  | `` | `` |
| 20 | `UT_DESC18` | `char(60)` | YES |  |  | `` | `` |
| 21 | `UT_DESC19` | `char(60)` | YES |  |  | `` | `` |
| 22 | `UT_DESC20` | `char(60)` | YES |  |  | `` | `` |
| 23 | `RSV_1` | `char(60)` | YES |  |  | `` | `` |
| 24 | `RSV_2` | `char(60)` | YES |  |  | `` | `` |
| 25 | `RSV_3` | `char(60)` | YES |  |  | `` | `` |
| 26 | `RSV_4` | `char(60)` | YES |  |  | `` | `` |
| 27 | `RSV_5` | `char(60)` | YES |  |  | `` | `` |
| 28 | `RSV_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `RSV_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `RSV_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `RSV_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 32 | `RSV_10` | `decimal(21,6)` | YES |  |  | `` | `` |

## 17. `[dbo].[orders]`

- Rows: `68624`
- Columns: `109`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ORD_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 3 | `ORD_DT` | `int` | YES |  |  | `` | `` |
| 4 | `ORD_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `PAID_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `INVS_TAX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `TAX_RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `MISC_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 12 | `SALES_NUM` | `char(4)` | YES |  |  | `` | `` |
| 13 | `SALES_NUM2` | `char(4)` | YES |  |  | `` | `` |
| 14 | `ORD_TIME` | `decimal(8,0)` | YES |  |  | `` | `` |
| 15 | `SP_SM_ADR` | `char(1)` | YES |  |  | `` | `` |
| 16 | `PO_NUM` | `char(100)` | YES |  |  | `` | `` |
| 17 | `SHIP_CD` | `tinyint` | YES |  |  | `` | `` |
| 18 | `CLOSE_CD` | `tinyint` | YES |  |  | `` | `` |
| 19 | `SHIP_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 20 | `TERM_DESC` | `char(15)` | YES |  |  | `` | `` |
| 21 | `TERMS_DAY` | `decimal(5,0)` | YES |  |  | `` | `` |
| 22 | `TERMS_COD` | `char(1)` | YES |  |  | `` | `` |
| 23 | `CC_PRINT` | `tinyint` | YES |  |  | `` | `` |
| 24 | `SP_ADR` | `char(60)` | YES |  |  | `` | `` |
| 25 | `SP_ADR_2` | `char(60)` | YES |  |  | `` | `` |
| 26 | `SP_ADR_22` | `char(60)` | YES |  |  | `` | `` |
| 27 | `SP_ADR_3` | `char(60)` | YES |  |  | `` | `` |
| 28 | `SP_ADR_CT` | `char(35)` | YES |  |  | `` | `` |
| 29 | `SP_ADR_ST` | `char(15)` | YES |  |  | `` | `` |
| 30 | `SP_ADR_ZP` | `char(15)` | YES |  |  | `` | `` |
| 31 | `NT_SEL` | `char(1)` | YES |  |  | `` | `` |
| 32 | `COMM_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 33 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 34 | `COMM_AMT2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 35 | `COMM_RT2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 36 | `CAN_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 37 | `ATTN` | `char(30)` | YES |  |  | `` | `` |
| 38 | `SHIP_DESC` | `char(15)` | YES |  |  | `` | `` |
| 39 | `FOB_DESC` | `char(15)` | YES |  |  | `` | `` |
| 40 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 41 | `REF_NUM` | `char(20)` | YES |  |  | `` | `` |
| 42 | `ORD_BY` | `char(15)` | YES |  |  | `` | `` |
| 43 | `CHK_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 44 | `ACT_NUM` | `tinyint` | YES |  |  | `` | `` |
| 45 | `STORE_NUM` | `char(12)` | YES |  |  | `` | `` |
| 46 | `INVS_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 47 | `NUM_CTL` | `decimal(5,0)` | YES |  |  | `` | `` |
| 48 | `TAXABLE_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 49 | `ORD_TYPE` | `char(2)` | YES |  |  | `` | `` |
| 50 | `COD_DESC` | `char(1)` | YES |  |  | `` | `` |
| 51 | `CC_NUM` | `char(20)` | YES |  |  | `` | `` |
| 52 | `CC_EXP` | `decimal(8,0)` | YES |  |  | `` | `` |
| 53 | `CC_PRV` | `char(12)` | YES |  |  | `` | `` |
| 54 | `CC_HOLD` | `char(20)` | YES |  |  | `` | `` |
| 55 | `PACK_PRT` | `decimal(5,0)` | YES |  |  | `` | `` |
| 56 | `ORD_PRT` | `decimal(5,0)` | YES |  |  | `` | `` |
| 57 | `SALES_NUM3` | `char(4)` | YES |  |  | `` | `` |
| 58 | `SALES_NUM4` | `char(4)` | YES |  |  | `` | `` |
| 59 | `COMM_AMT3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 60 | `COMM_RT3` | `decimal(5,2)` | YES |  |  | `` | `` |
| 61 | `COMM_AMT4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 62 | `COMM_RT4` | `decimal(5,2)` | YES |  |  | `` | `` |
| 63 | `MGR_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 64 | `MGR_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 65 | `ASM_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 66 | `ASM_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 67 | `INV_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 68 | `INV_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 69 | `MISC_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 70 | `MISC_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 71 | `QC_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 72 | `QC_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 73 | `TS_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 74 | `TS_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 75 | `ACT_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 76 | `ACT_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 77 | `SLS_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 78 | `SLS_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 79 | `RMA_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 80 | `RMA_PROV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 81 | `PCK_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 82 | `SOUR_DESC` | `char(8)` | YES |  |  | `` | `` |
| 83 | `SP_ADR_CN` | `char(40)` | YES |  |  | `` | `` |
| 84 | `CURRENCY` | `char(10)` | YES |  |  | `` | `` |
| 85 | `EXC_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 86 | `SHIP_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 87 | `AUTHRZ_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 88 | `EMAIL_ADR` | `char(60)` | YES |  |  | `` | `` |
| 89 | `EMAIL_IND` | `char(1)` | YES |  |  | `` | `` |
| 90 | `COD_CASH` | `char(1)` | YES |  |  | `` | `` |
| 91 | `TRK_NUM` | `char(30)` | YES |  |  | `` | `` |
| 92 | `ORDER_BY` | `char(10)` | YES |  |  | `` | `` |
| 93 | `CUS_SHIP_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 94 | `DISC_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 95 | `UPDT_BY` | `char(10)` | YES |  |  | `` | `` |
| 96 | `UPDT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 97 | `PCODE` | `char(21)` | YES |  |  | `` | `` |
| 98 | `UPS_ACT` | `char(25)` | YES |  |  | `` | `` |
| 99 | `SP_CUS_NM` | `char(60)` | YES |  |  | `` | `` |
| 100 | `SOLD_TO` | `char(50)` | YES |  |  | `` | `` |
| 101 | `STATUS` | `char(20)` | YES |  |  | `` | `` |
| 102 | `EARN_BONUS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 103 | `USED_BONUS` | `decimal(15,4)` | YES |  |  | `` | `` |
| 104 | `BONUS_BACK` | `decimal(15,4)` | YES |  |  | `` | `` |
| 105 | `PAYMT_CD` | `int` | YES |  |  | `` | `` |
| 106 | `CUS_SHIP_TEL2` | `varchar(19)` | YES |  |  | `` | `` |
| 107 | `REF_NUM2` | `varchar(20)` | YES |  |  | `` | `` |
| 108 | `DELIVERY_DT` | `int` | YES |  |  | `` | `` |
| 109 | `Id` | `int` | NO | YES | YES | `` | `` |

## 18. `[dbo].[iadj_log]`

- Rows: `59655`
- Columns: `42`
- Primary key: `BAT_NUM`, `NT_NUM`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BAT_NUM` | `int` | NO |  | YES | `` | `` |
| 2 | `ADJ_TYPE` | `char(20)` | YES |  |  | `` | `` |
| 3 | `LOG_DT` | `int` | YES |  |  | `` | `` |
| 4 | `LOG_TIME` | `int` | YES |  |  | `` | `` |
| 5 | `INVS_NUM` | `int` | YES |  |  | `` | `` |
| 6 | `INVS_CD` | `tinyint` | YES |  |  | `` | `` |
| 7 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 8 | `PROD_CD` | `char(21)` | YES |  |  | `` | `` |
| 9 | `PROD_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `UNIT_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `REAL_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `LOG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `PROD_COMP` | `char(1)` | YES |  |  | `` | `` |
| 16 | `TERM_LN` | `tinyint` | YES |  |  | `` | `` |
| 17 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `UT_DISC` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `COMM_LN` | `int` | YES |  |  | `` | `` |
| 20 | `ORD_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 21 | `NT_NUM` | `int` | NO |  | YES | `` | `` |
| 22 | `UT_SER` | `char(1)` | YES |  |  | `` | `` |
| 23 | `UT_DESC` | `char(60)` | YES |  |  | `` | `` |
| 24 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 25 | `TAX_IND` | `char(1)` | YES |  |  | `` | `` |
| 26 | `UT_NT` | `char(1)` | YES |  |  | `` | `` |
| 27 | `SO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `DISC_LINE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `PC_UNIT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `DEF_UT` | `char(2)` | YES |  |  | `` | `` |
| 31 | `REF_NUM` | `char(15)` | YES |  |  | `` | `` |
| 32 | `DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 33 | `SHIP` | `decimal(21,6)` | YES |  |  | `` | `` |
| 34 | `HNDL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 35 | `EXT_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 36 | `IN_STOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `PRICE_BASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `FRT_CUS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `PROD_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 40 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 41 | `MISC_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 42 | `AVG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |

## 19. `[dbo].[bin_invs]`

- Rows: `55423`
- Columns: `10`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 3 | `NT_NUM` | `smallint` | NO |  |  | `` | `` |
| 4 | `PROD_CD` | `char(20)` | NO |  |  | `` | `` |
| 5 | `WHS_NUM` | `char(8)` | NO |  |  | `` | `` |
| 6 | `BIN_CD` | `char(16)` | NO |  |  | `` | `` |
| 7 | `INVS_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `COMM_LN` | `decimal(8,0)` | YES |  |  | `` | `` |
| 9 | `PRICE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `COST` | `decimal(21,6)` | YES |  |  | `` | `` |

## 20. `[dbo].[bnk_rlog]`

- Rows: `52513`
- Columns: `20`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BANK_TYPE` | `int` | NO |  |  | `` | `` |
| 2 | `BANK_NUM` | `int` | NO |  |  | `` | `` |
| 3 | `STM_DT` | `int` | NO |  |  | `` | `` |
| 4 | `COMM_LN` | `int` | NO |  |  | `` | `` |
| 5 | `CHK_TYPE` | `char(2)` | YES |  |  | `` | `` |
| 6 | `CHK_NUM` | `char(30)` | NO |  |  | `` | `` |
| 7 | `VEND_ID` | `char(20)` | YES |  |  | `` | `` |
| 8 | `CHK_TRS` | `smallint` | YES |  |  | `` | `` |
| 9 | `CHK_AMT` | `decimal(15,2)` | YES |  |  | `` | `` |
| 10 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 11 | `SELECT_SW` | `tinyint` | YES |  |  | `` | `` |
| 12 | `EDIT_FLAG` | `tinyint` | YES |  |  | `` | `` |
| 13 | `TRS_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 14 | `TYPE_CD` | `int` | YES |  |  | `` | `` |
| 15 | `INVS_NUM` | `char(16)` | YES |  |  | `` | `` |
| 16 | `INVS_CD` | `tinyint` | YES |  |  | `` | `` |
| 17 | `CUS_ID` | `char(10)` | YES |  |  | `` | `` |
| 18 | `CHK_DT` | `int` | YES |  |  | `` | `` |
| 19 | `CHK_CD` | `int` | NO |  |  | `` | `` |
| 20 | `VNM_LST` | `char(50)` | YES |  |  | `` | `` |

## 21. `[dbo].[zipfile]`

- Rows: `42620`
- Columns: `3`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ZIPCODE` | `char(5)` | NO |  |  | `` | `` |
| 2 | `ZIPCITY` | `char(25)` | YES |  |  | `` | `` |
| 3 | `ZIPST` | `char(2)` | YES |  |  | `` | `` |

## 22. `[dbo].[cus_ssm]`

- Rows: `38000`
- Columns: `30`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `SLS_YEAR` | `decimal(5,0)` | YES |  |  | `` | `` |
| 3 | `TYPE` | `tinyint` | NO |  |  | `` | `` |
| 4 | `CURT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 5 | `LAST_PDT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 6 | `SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `COST_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `COST_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `COST_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `COST_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `COST_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `COST_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `COST_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `COST_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `COST_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `COST_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `COST_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `COST_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `Id` | `int` | NO | YES | YES | `` | `` |

## 23. `[dbo].[iadjfile]`

- Rows: `33533`
- Columns: `11`
- Primary key: `BAT_NUM`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BAT_NUM` | `int` | NO |  | YES | `` | `` |
| 2 | `ADJ_TYPE` | `char(20)` | YES |  |  | `` | `` |
| 3 | `LOG_DT` | `int` | YES |  |  | `` | `` |
| 4 | `LOG_TIME` | `int` | YES |  |  | `` | `` |
| 5 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 6 | `VEND_INVS` | `char(20)` | YES |  |  | `` | `` |
| 7 | `UPDATE_DT` | `int` | YES |  |  | `` | `` |
| 8 | `UPDATE_TM` | `int` | YES |  |  | `` | `` |
| 9 | `UPDATE_BY` | `char(10)` | YES |  |  | `` | `` |
| 10 | `INVS_NUM` | `int` | YES |  |  | `` | `` |
| 11 | `INVS_CD` | `tinyint` | YES |  |  | `` | `` |

## 24. `[dbo].[cus_bls]`

- Rows: `30509`
- Columns: `17`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `BAL_DT` | `int` | NO |  |  | `` | `` |
| 3 | `BAL_TM` | `int` | YES |  |  | `` | `` |
| 4 | `INVS_TTL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `PAID_TTL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `CRD_TTL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `BLS_TTL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `BLS_CURT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `BLS_30` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `BLS_60` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `BLS_90` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `BLS_180` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `BLS_365` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `BLS_366` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `INS_CNT` | `int` | YES |  |  | `` | `` |
| 16 | `DUE_CNT` | `int` | YES |  |  | `` | `` |
| 17 | `CRD_CNT` | `int` | YES |  |  | `` | `` |

## 25. `[dbo].[bin_file]`

- Rows: `29500`
- Columns: `28`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(20)` | NO |  |  | `` | `` |
| 2 | `WHS_NUM` | `char(8)` | NO |  |  | `` | `` |
| 3 | `BIN_CD` | `char(16)` | NO |  |  | `` | `` |
| 4 | `IN_STOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `BACK_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `ON_ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `WIP_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `RMA_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `WATER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `ORDERSIZE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `MINSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `MAXSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `UPDT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 15 | `PHYC_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 16 | `UPDT_BY` | `char(8)` | YES |  |  | `` | `` |
| 17 | `LT_SL_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 18 | `VENDOR` | `char(10)` | YES |  |  | `` | `` |
| 19 | `PRICE_BASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `FRT_CUS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `HNDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `PROD_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `AVG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `SALES_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `IMAGE_NM` | `char(100)` | YES |  |  | `` | `` |
| 26 | `UPC_NUM` | `char(30)` | YES |  |  | `` | `` |
| 27 | `LOT_NUM` | `char(20)` | YES |  |  | `` | `` |
| 28 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |

## 26. `[dbo].[bnk_dpst]`

- Rows: `28902`
- Columns: `16`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BANK_NUM` | `tinyint` | YES |  |  | `` | `` |
| 2 | `DEP_NUM` | `int` | NO |  |  | `` | `` |
| 3 | `DEP_DT` | `int` | YES |  |  | `` | `` |
| 4 | `DEP_TM` | `int` | YES |  |  | `` | `` |
| 5 | `TRS_DT_FM` | `int` | YES |  |  | `` | `` |
| 6 | `TRS_DT_TO` | `int` | YES |  |  | `` | `` |
| 7 | `DEP_BY` | `char(10)` | YES |  |  | `` | `` |
| 8 | `NUM_CHK` | `smallint` | YES |  |  | `` | `` |
| 9 | `CHK_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `NUM_CASH` | `smallint` | YES |  |  | `` | `` |
| 11 | `CASH_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `NUM_OTHER` | `smallint` | YES |  |  | `` | `` |
| 13 | `OTHER_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `BUS_CD` | `int` | YES |  |  | `` | `` |
| 15 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 16 | `POST_SW` | `tinyint` | YES |  |  | `` | `` |

## 27. `[dbo].[bnk_cldp]`

- Rows: `28381`
- Columns: `12`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 2 | `BANK_NUM` | `int` | NO |  |  | `` | `` |
| 3 | `STM_DT` | `int` | YES |  |  | `` | `` |
| 4 | `CUS_ID` | `char(12)` | YES |  |  | `` | `` |
| 5 | `CHK_NUM` | `char(30)` | NO |  |  | `` | `` |
| 6 | `CHK_CD` | `int` | YES |  |  | `` | `` |
| 7 | `CHK_AMT` | `decimal(19,3)` | YES |  |  | `` | `` |
| 8 | `STATUS_CD` | `tinyint` | YES |  |  | `` | `` |
| 9 | `DEP_DT` | `int` | YES |  |  | `` | `` |
| 10 | `INVS_NUM` | `int` | YES |  |  | `` | `` |
| 11 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 12 | `TRS_TYPE` | `int` | YES |  |  | `` | `` |

## 28. `[dbo].[msc_file]`

- Rows: `27947`
- Columns: `5`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `SCN_NM` | `char(3)` | NO |  |  | `` | `` |
| 2 | `SCN_NUM` | `char(10)` | NO |  |  | `` | `` |
| 3 | `COMM_LN` | `decimal(8,0)` | YES |  |  | `` | `` |
| 4 | `STRING_1` | `char(100)` | YES |  |  | `` | `` |
| 5 | `DECIMAL_1` | `decimal(21,6)` | YES |  |  | `` | `` |

## 29. `[dbo].[product_sync_backup_20241219]`

- Rows: `27494`
- Columns: `7`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `varchar(50)` | NO |  |  | `` | `` |
| 2 | `CATEGORY_NAME` | `varchar(max)` | YES |  |  | `` | `` |
| 3 | `CATEGORY_COUNT` | `int` | YES |  |  | `` | `` |
| 4 | `STOCK_STATUS` | `varchar(50)` | YES |  |  | `` | `` |
| 5 | `LAST_SYNC` | `datetime` | YES |  |  | `` | `` |
| 6 | `DATE_AVAILABLE` | `date` | YES |  |  | `` | `` |
| 7 | `PRODUCT_STATUS` | `varchar(20)` | YES |  |  | `` | `` |

## 30. `[dbo].[inv_divs]`

- Rows: `25840`
- Columns: `17`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(20)` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 4 | `DIV_CD` | `char(10)` | YES |  |  | `` | `` |
| 5 | `PRJ_CD` | `char(10)` | YES |  |  | `` | `` |
| 6 | `JOB_CD` | `char(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_CD` | `char(10)` | YES |  |  | `` | `` |
| 8 | `CLASS_CD` | `char(20)` | YES |  |  | `` | `` |
| 9 | `REG_CD` | `char(10)` | YES |  |  | `` | `` |
| 10 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 11 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `CHT_NUM2` | `int` | YES |  |  | `` | `` |
| 13 | `CHT_NUM3` | `int` | YES |  |  | `` | `` |
| 14 | `RSV_1` | `decimal(21,3)` | YES |  |  | `` | `` |
| 15 | `RSV_2` | `decimal(21,3)` | YES |  |  | `` | `` |
| 16 | `RSV_3` | `char(60)` | YES |  |  | `` | `` |
| 17 | `RSV_4` | `char(60)` | YES |  |  | `` | `` |

## 31. `[dbo].[inv_detl]`

- Rows: `25837`
- Columns: `24`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `CASE_LEN` | `decimal(21,4)` | YES |  |  | `` | `` |
| 3 | `CASE_HI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 4 | `CASE_WI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 5 | `CASE_WT` | `decimal(21,4)` | YES |  |  | `` | `` |
| 6 | `BOX_LEN` | `decimal(21,4)` | YES |  |  | `` | `` |
| 7 | `BOX_HI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 8 | `BOX_WI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 9 | `BOX_WT` | `decimal(21,4)` | YES |  |  | `` | `` |
| 10 | `UT_LEN` | `decimal(21,4)` | YES |  |  | `` | `` |
| 11 | `UT_HI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 12 | `UT_WI` | `decimal(21,4)` | YES |  |  | `` | `` |
| 13 | `UT_WT` | `decimal(21,4)` | YES |  |  | `` | `` |
| 14 | `PD_KG` | `tinyint` | YES |  |  | `` | `` |
| 15 | `ORIGEN` | `char(20)` | YES |  |  | `` | `` |
| 16 | `MFG_NUM` | `char(30)` | YES |  |  | `` | `` |
| 17 | `CASE_128` | `char(30)` | YES |  |  | `` | `` |
| 18 | `BOX_128` | `char(30)` | YES |  |  | `` | `` |
| 19 | `UNIT_128` | `char(30)` | YES |  |  | `` | `` |
| 20 | `RESV_1` | `char(40)` | YES |  |  | `` | `` |
| 21 | `RESV_2` | `char(40)` | YES |  |  | `` | `` |
| 22 | `RESV_3` | `char(40)` | YES |  |  | `` | `` |
| 23 | `RESV_4` | `char(40)` | YES |  |  | `` | `` |
| 24 | `Id` | `int` | NO | YES | YES | `` | `` |

## 32. `[dbo].[inv_note]`

- Rows: `25837`
- Columns: `15`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `NOTE_LN1` | `char(400)` | YES |  |  | `` | `` |
| 3 | `NOTE_LN2` | `char(400)` | YES |  |  | `` | `` |
| 4 | `NOTE_LN3` | `char(400)` | YES |  |  | `` | `` |
| 5 | `NOTE_LN4` | `char(400)` | YES |  |  | `` | `` |
| 6 | `NOTE_LN5` | `char(400)` | YES |  |  | `` | `` |
| 7 | `NOTE_LN6` | `char(400)` | YES |  |  | `` | `` |
| 8 | `NOTE_LN7` | `char(400)` | YES |  |  | `` | `` |
| 9 | `NOTE_LN8` | `char(400)` | YES |  |  | `` | `` |
| 10 | `RESERVED1` | `char(80)` | YES |  |  | `` | `` |
| 11 | `RESERVED2` | `char(80)` | YES |  |  | `` | `` |
| 12 | `RESERVED3` | `char(80)` | YES |  |  | `` | `` |
| 13 | `RESERVED4` | `char(80)` | YES |  |  | `` | `` |
| 14 | `RESERVED5` | `char(80)` | YES |  |  | `` | `` |
| 15 | `Id` | `int` | NO | YES | YES | `` | `` |

## 33. `[dbo].[prod_sls]`

- Rows: `25592`
- Columns: `110`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `CURT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 3 | `LAST_2_QTY_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 4 | `LAST_2_QTY_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `LAST_2_QTY_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `LAST_2_QTY_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `LAST_2_QTY_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `LAST_2_QTY_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `LAST_2_QTY_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `LAST_2_QTY_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `LAST_2_QTY_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `LAST_2_QTY_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `LAST_2_QTY_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `LAST_2_QTY_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `LAST_QTY_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `LAST_QTY_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `LAST_QTY_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `LAST_QTY_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `LAST_QTY_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `LAST_QTY_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `LAST_QTY_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `LAST_QTY_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `LAST_QTY_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `LAST_QTY_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `LAST_QTY_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `LAST_QTY_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `THIS_QTY_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `THIS_QTY_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `THIS_QTY_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `THIS_QTY_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `THIS_QTY_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 32 | `THIS_QTY_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 33 | `THIS_QTY_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 34 | `THIS_QTY_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 35 | `THIS_QTY_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 36 | `THIS_QTY_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `THIS_QTY_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `THIS_QTY_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `LAST_2_RTN_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 40 | `LAST_2_RTN_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 41 | `LAST_2_RTN_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 42 | `LAST_2_RTN_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 43 | `LAST_2_RTN_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 44 | `LAST_2_RTN_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 45 | `LAST_2_RTN_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 46 | `LAST_2_RTN_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 47 | `LAST_2_RTN_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 48 | `LAST_2_RTN_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 49 | `LAST_2_RTN_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 50 | `LAST_2_RTN_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 51 | `LAST_RTN_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 52 | `LAST_RTN_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 53 | `LAST_RTN_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 54 | `LAST_RTN_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 55 | `LAST_RTN_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 56 | `LAST_RTN_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 57 | `LAST_RTN_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 58 | `LAST_RTN_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 59 | `LAST_RTN_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 60 | `LAST_RTN_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 61 | `LAST_RTN_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 62 | `LAST_RTN_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 63 | `THIS_RTN_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 64 | `THIS_RTN_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 65 | `THIS_RTN_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 66 | `THIS_RTN_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 67 | `THIS_RTN_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 68 | `THIS_RTN_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 69 | `THIS_RTN_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 70 | `THIS_RTN_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 71 | `THIS_RTN_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 72 | `THIS_RTN_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 73 | `THIS_RTN_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 74 | `THIS_RTN_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 75 | `LAST_2_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 76 | `LAST_2_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 77 | `LAST_2_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 78 | `LAST_2_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 79 | `LAST_2_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 80 | `LAST_2_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 81 | `LAST_2_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 82 | `LAST_2_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 83 | `LAST_2_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 84 | `LAST_2_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 85 | `LAST_2_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 86 | `LAST_2_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 87 | `LAST_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 88 | `LAST_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 89 | `LAST_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 90 | `LAST_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 91 | `LAST_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 92 | `LAST_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 93 | `LAST_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 94 | `LAST_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 95 | `LAST_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 96 | `LAST_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 97 | `LAST_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 98 | `LAST_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 99 | `THIS_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 100 | `THIS_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 101 | `THIS_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 102 | `THIS_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 103 | `THIS_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 104 | `THIS_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 105 | `THIS_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 106 | `THIS_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 107 | `THIS_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 108 | `THIS_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 109 | `THIS_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 110 | `THIS_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |

## 34. `[dbo].[inv_upc]`

- Rows: `23245`
- Columns: `4`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `UPC_CD` | `char(20)` | NO |  |  | `` | `` |
| 3 | `UPC_TYPE` | `char(10)` | YES |  |  | `` | `` |
| 4 | `SEQ_NUM` | `int` | YES |  |  | `` | `` |

## 35. `[dbo].[inv_data]`

- Rows: `20080`
- Columns: `61`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `WHS_NUM` | `char(8)` | NO |  |  | `` | `` |
| 3 | `IN_STOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 4 | `LASTRCV_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `LASTRCV_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 6 | `PRICE_BASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `FRT_CUS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `PROD_DUTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `MISC_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `AVG_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `LT_SL_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 13 | `VENDOR` | `char(10)` | YES |  |  | `` | `` |
| 14 | `LST_ORDER` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `ORD_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 16 | `STK_IND` | `char(1)` | YES |  |  | `` | `` |
| 17 | `BACK_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `ON_ORDER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `WIP_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `RMA_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `WATER_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `ORDERSIZE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `MINSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `INV_LOC` | `char(20)` | YES |  |  | `` | `` |
| 26 | `UNIT_COLOR` | `char(11)` | YES |  |  | `` | `` |
| 27 | `CLASS_CD` | `char(20)` | YES |  |  | `` | `` |
| 28 | `DESCRIP` | `char(61)` | YES |  |  | `` | `` |
| 29 | `DEF_UNIT` | `char(2)` | YES |  |  | `` | `` |
| 30 | `UPDT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 31 | `PHYC_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 32 | `IMAGE_NM` | `char(80)` | YES |  |  | `` | `` |
| 33 | `OEM_CD` | `char(20)` | YES |  |  | `` | `` |
| 34 | `ALT_CD` | `char(20)` | YES |  |  | `` | `` |
| 35 | `UPDT_BY` | `char(8)` | YES |  |  | `` | `` |
| 36 | `CURRENCY_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `COST_FACTOR` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `MAXSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `QTYH` | `decimal(21,6)` | YES |  |  | `` | `` |
| 40 | `QTYW` | `decimal(21,6)` | YES |  |  | `` | `` |
| 41 | `QTYL` | `decimal(21,6)` | YES |  |  | `` | `` |
| 42 | `LOT_NUM` | `char(20)` | YES |  |  | `` | `` |
| 43 | `UPC_NUM` | `char(20)` | YES |  |  | `` | `` |
| 44 | `PROD_CLR` | `char(20)` | YES |  |  | `` | `` |
| 45 | `SZ_RUN` | `char(20)` | YES |  |  | `` | `` |
| 46 | `EXP_DATE` | `int` | YES |  |  | `` | `` |
| 47 | `EXCHG_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 48 | `O_TYPE` | `char(20)` | YES |  |  | `` | `` |
| 49 | `O_PRICE_BASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 50 | `O_FRT_CUS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 51 | `O_HNDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 52 | `ORIGAN` | `char(20)` | YES |  |  | `` | `` |
| 53 | `UPC_CD` | `char(30)` | YES |  |  | `` | `` |
| 54 | `INV_TYPE` | `char(8)` | YES |  |  | `` | `` |
| 55 | `WO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 56 | `POS_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 57 | `STK_XXX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 58 | `Id` | `int` | NO | YES | YES | `` | `` |
| 59 | `msrepl_tran_version` | `uniqueidentifier` | NO |  |  | `(newid())` | `` |
| 60 | `BASELINE_QTY` | `decimal(21,6)` | YES |  |  | `((0))` | `` |
| 61 | `BASELINE_DT` | `int` | YES |  |  | `((0))` | `` |

## 36. `[dbo].[apmtnote]`

- Rows: `19660`
- Columns: `4`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `NT_TYPE` | `tinyint` | NO |  |  | `` | `` |
| 2 | `VEND_ID` | `char(11)` | NO |  |  | `` | `` |
| 3 | `NT_NUM` | `char(10)` | NO |  |  | `` | `` |
| 4 | `NOTE_TX` | `char(1024)` | YES |  |  | `` | `` |

## 37. `[dbo].[bnk_clck]`

- Rows: `18387`
- Columns: `6`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BANK_NUM` | `tinyint` | NO |  |  | `` | `` |
| 2 | `STM_DT` | `int` | YES |  |  | `` | `` |
| 3 | `CHK_NUM` | `decimal(21,3)` | NO |  |  | `` | `` |
| 4 | `CHK_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `STATUS_CD` | `tinyint` | YES |  |  | `` | `` |
| 6 | `TYPE_CD` | `smallint` | YES |  |  | `` | `` |

## 38. `[dbo].[pbl_dist]`

- Rows: `17369`
- Columns: `10`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `VEND_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `INVS_NUM` | `char(10)` | NO |  |  | `` | `` |
| 3 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 4 | `CHT_NUM` | `char(15)` | YES |  |  | `` | `` |
| 5 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 6 | `CHT_DESC` | `char(40)` | YES |  |  | `` | `` |
| 7 | `MEMO_LN` | `char(40)` | YES |  |  | `` | `` |
| 8 | `CHT_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `INS_VAL` | `tinyint` | YES |  |  | `` | `` |
| 10 | `COMM_LN` | `int` | NO |  |  | `` | `` |

## 39. `[dbo].[product_sync]`

- Rows: `17223`
- Columns: `7`
- Primary key: `PROD_CD`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `varchar(50)` | NO |  | YES | `` | `` |
| 2 | `CATEGORY_NAME` | `varchar(max)` | YES |  |  | `` | `` |
| 3 | `CATEGORY_COUNT` | `int` | YES |  |  | `` | `` |
| 4 | `STOCK_STATUS` | `varchar(50)` | YES |  |  | `` | `` |
| 5 | `LAST_SYNC` | `datetime` | YES |  |  | `(getdate())` | `` |
| 7 | `DATE_AVAILABLE` | `date` | YES |  |  | `` | `` |
| 8 | `PRODUCT_STATUS` | `varchar(20)` | YES |  |  | `` | `` |

## 40. `[dbo].[acct_mst]`

- Rows: `17216`
- Columns: `15`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ACCT_NUM` | `char(11)` | NO |  |  | `` | `` |
| 2 | `CURT_BLS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 3 | `LAST_BDT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 4 | `BL_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `CRD_MEMO` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `MAX_BLS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `LAST_PDT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 8 | `LAST_ODT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 9 | `ORD_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `BILL_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 11 | `PMT_DAY` | `decimal(8,0)` | YES |  |  | `` | `` |
| 12 | `PMT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 13 | `Id` | `int` | NO | YES | YES | `` | `` |
| 14 | `PMT_AVG` | `int` | YES |  |  | `` | `` |
| 15 | `PMT_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |

## 41. `[dbo].[cus_divs]`

- Rows: `17201`
- Columns: `18`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(10)` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 4 | `DIV_CD` | `char(10)` | YES |  |  | `` | `` |
| 5 | `PRJ_CD` | `char(10)` | YES |  |  | `` | `` |
| 6 | `JOB_CD` | `char(10)` | YES |  |  | `` | `` |
| 7 | `DEPT_CD` | `char(10)` | YES |  |  | `` | `` |
| 8 | `CLASS_CD` | `char(20)` | YES |  |  | `` | `` |
| 9 | `REG_CD` | `char(10)` | YES |  |  | `` | `` |
| 10 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 11 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `CHT_NUM2` | `int` | YES |  |  | `` | `` |
| 13 | `CHT_NUM3` | `int` | YES |  |  | `` | `` |
| 14 | `RSV_1` | `decimal(21,3)` | YES |  |  | `` | `` |
| 15 | `RSV_2` | `decimal(21,3)` | YES |  |  | `` | `` |
| 16 | `RSV_3` | `char(60)` | YES |  |  | `` | `` |
| 17 | `RSV_4` | `char(60)` | YES |  |  | `` | `` |
| 18 | `Id` | `int` | NO | YES | YES | `` | `` |

## 42. `[dbo].[customer]`

- Rows: `17130`
- Columns: `93`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_NM` | `char(41)` | YES |  |  | `` | `` |
| 2 | `CUS_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 3 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 4 | `ADDRESS` | `char(60)` | YES |  |  | `` | `` |
| 5 | `ADDRESS2` | `char(60)` | YES |  |  | `` | `` |
| 6 | `CITY` | `char(40)` | YES |  |  | `` | `` |
| 7 | `STATE` | `char(20)` | YES |  |  | `` | `` |
| 8 | `ZIP` | `char(16)` | YES |  |  | `` | `` |
| 9 | `COUNTRY` | `char(30)` | YES |  |  | `` | `` |
| 10 | `PHONE` | `char(25)` | YES |  |  | `` | `` |
| 11 | `PHONE_2` | `char(25)` | YES |  |  | `` | `` |
| 12 | `PHONE_3` | `char(25)` | YES |  |  | `` | `` |
| 13 | `ATTN` | `char(30)` | YES |  |  | `` | `` |
| 14 | `TITLE` | `char(10)` | YES |  |  | `` | `` |
| 15 | `ATTN_2` | `char(30)` | YES |  |  | `` | `` |
| 16 | `CRD_LMT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 17 | `SALES_NUM` | `char(5)` | YES |  |  | `` | `` |
| 18 | `SALES_NUM2` | `char(4)` | YES |  |  | `` | `` |
| 19 | `TERR_CD` | `char(8)` | YES |  |  | `` | `` |
| 20 | `FIRST_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 21 | `TERM` | `tinyint` | YES |  |  | `` | `` |
| 22 | `APPX_AMT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 23 | `TAX_RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `CUS_NT1` | `char(100)` | YES |  |  | `` | `` |
| 25 | `CUS_NT2` | `char(100)` | YES |  |  | `` | `` |
| 26 | `SALES_LS` | `char(25)` | YES |  |  | `` | `` |
| 27 | `SLS_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 28 | `COMM_RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `COMM_RATE2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `BAD_CHK_NUM` | `tinyint` | YES |  |  | `` | `` |
| 31 | `SHP_ADDRESS` | `char(60)` | YES |  |  | `` | `` |
| 32 | `SHP_ADDRESS2` | `char(60)` | YES |  |  | `` | `` |
| 33 | `SHP_CITY` | `char(40)` | YES |  |  | `` | `` |
| 34 | `SHP_STATE` | `char(20)` | YES |  |  | `` | `` |
| 35 | `SHP_ZIP` | `char(15)` | YES |  |  | `` | `` |
| 36 | `SHP_COUNTRY` | `char(30)` | YES |  |  | `` | `` |
| 37 | `PHN_EXT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 38 | `CRD_RATE` | `char(3)` | YES |  |  | `` | `` |
| 39 | `DEPT_NUM` | `char(10)` | YES |  |  | `` | `` |
| 40 | `CUS_SUR` | `char(8)` | YES |  |  | `` | `` |
| 41 | `EMAIL_ADR` | `char(240)` | YES |  |  | `` | `` |
| 42 | `WEB_ADR` | `char(40)` | YES |  |  | `` | `` |
| 43 | `CC_NUM` | `char(20)` | YES |  |  | `` | `` |
| 44 | `CC_EXP` | `decimal(8,0)` | YES |  |  | `` | `` |
| 45 | `CC_NAME` | `char(25)` | YES |  |  | `` | `` |
| 46 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 47 | `TERMS_DAY` | `decimal(5,0)` | YES |  |  | `` | `` |
| 48 | `TERMS_COD` | `char(1)` | YES |  |  | `` | `` |
| 49 | `TERM_DESC` | `char(15)` | YES |  |  | `` | `` |
| 50 | `IMAGE_NM` | `char(200)` | YES |  |  | `` | `` |
| 51 | `SOURCE_DESC` | `char(8)` | YES |  |  | `` | `` |
| 52 | `SHIP_DESC` | `char(15)` | YES |  |  | `` | `` |
| 53 | `PRIORITY` | `char(2)` | YES |  |  | `` | `` |
| 54 | `DUN_NUM` | `char(15)` | YES |  |  | `` | `` |
| 55 | `PHONE_4` | `char(25)` | YES |  |  | `` | `` |
| 56 | `SHIP_SPE` | `tinyint` | YES |  |  | `` | `` |
| 57 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 58 | `DB_NUM` | `char(15)` | YES |  |  | `` | `` |
| 59 | `REF_NUM` | `char(15)` | YES |  |  | `` | `` |
| 60 | `SHIP_OPT` | `tinyint` | YES |  |  | `` | `` |
| 61 | `RETAIL_STR` | `tinyint` | YES |  |  | `` | `` |
| 62 | `GRP_ID` | `char(11)` | YES |  |  | `` | `` |
| 63 | `RSV_1` | `char(11)` | YES |  |  | `` | `` |
| 64 | `FAC_NM` | `char(20)` | YES |  |  | `` | `` |
| 65 | `FAC_ACT` | `char(20)` | YES |  |  | `` | `` |
| 66 | `FAC_LMT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 67 | `SALES_NUM3` | `char(4)` | YES |  |  | `` | `` |
| 68 | `SALES_NUM4` | `char(4)` | YES |  |  | `` | `` |
| 69 | `COMM_RT3` | `decimal(5,2)` | YES |  |  | `` | `` |
| 70 | `COMM_RT4` | `decimal(5,2)` | YES |  |  | `` | `` |
| 71 | `PCODE` | `char(21)` | YES |  |  | `` | `` |
| 72 | `IS_EDI_CUS` | `tinyint` | YES |  |  | `` | `` |
| 73 | `IS_CAN_ORD` | `tinyint` | YES |  |  | `` | `` |
| 74 | `AREA_CD` | `char(30)` | YES |  |  | `` | `` |
| 75 | `FIRST_NM` | `char(30)` | YES |  |  | `` | `` |
| 76 | `LAST_NM` | `char(30)` | YES |  |  | `` | `` |
| 77 | `SHP_CUS_NM` | `char(60)` | YES |  |  | `` | `` |
| 78 | `SHP_FIRST_NM` | `char(30)` | YES |  |  | `` | `` |
| 79 | `SHP_LAST_NM` | `char(30)` | YES |  |  | `` | `` |
| 80 | `SHP_PHONE` | `char(25)` | YES |  |  | `` | `` |
| 81 | `SHP_PHONE_3` | `char(25)` | YES |  |  | `` | `` |
| 82 | `SHP_PHONE_2` | `char(25)` | YES |  |  | `` | `` |
| 83 | `SHP_EMAIL_ADR` | `char(80)` | YES |  |  | `` | `` |
| 84 | `PHONE_5` | `char(25)` | YES |  |  | `` | `` |
| 85 | `SHP_PHONE_5` | `char(25)` | YES |  |  | `` | `` |
| 86 | `PDF_NM` | `char(200)` | YES |  |  | `` | `` |
| 87 | `DS_NUM` | `char(25)` | YES |  |  | `` | `` |
| 88 | `FNAME` | `char(30)` | YES |  |  | `` | `` |
| 89 | `LNAME` | `char(30)` | YES |  |  | `` | `` |
| 90 | `SHP_FNAME` | `char(30)` | YES |  |  | `` | `` |
| 91 | `SHP_LNAME` | `char(30)` | YES |  |  | `` | `` |
| 92 | `Id` | `int` | NO | YES | YES | `` | `` |
| 93 | `SERVICE_CODE` | `char(20)` | YES |  |  | `` | `` |

## 43. `[dbo].[cus_sls]`

- Rows: `16992`
- Columns: `39`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `CURT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 3 | `LAST_PDT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 4 | `LAST_2_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `LAST_2_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `LAST_2_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `LAST_2_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `LAST_2_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `LAST_2_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `LAST_2_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `LAST_2_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `LAST_2_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `LAST_2_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `LAST_2_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `LAST_2_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `LAST_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `LAST_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `LAST_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `LAST_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `LAST_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `LAST_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `LAST_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `LAST_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `LAST_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 25 | `LAST_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `LAST_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `LAST_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |
| 28 | `THIS_SLS_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `THIS_SLS_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `THIS_SLS_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `THIS_SLS_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 32 | `THIS_SLS_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 33 | `THIS_SLS_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 34 | `THIS_SLS_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 35 | `THIS_SLS_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 36 | `THIS_SLS_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `THIS_SLS_10` | `decimal(21,6)` | YES |  |  | `` | `` |
| 38 | `THIS_SLS_11` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `THIS_SLS_12` | `decimal(21,6)` | YES |  |  | `` | `` |

## 44. `[dbo].[cus_crd]`

- Rows: `16755`
- Columns: `14`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `BANK_NM` | `char(30)` | YES |  |  | `` | `` |
| 3 | `CK_ACT` | `char(30)` | YES |  |  | `` | `` |
| 4 | `SV_ACT` | `char(30)` | YES |  |  | `` | `` |
| 5 | `BANK_PHN` | `char(25)` | YES |  |  | `` | `` |
| 6 | `REF_ACT1` | `char(60)` | YES |  |  | `` | `` |
| 7 | `REF_ACT2` | `char(60)` | YES |  |  | `` | `` |
| 8 | `REF_ACT3` | `char(60)` | YES |  |  | `` | `` |
| 9 | `REF_ACT4` | `char(60)` | YES |  |  | `` | `` |
| 10 | `BK_ADR` | `char(40)` | YES |  |  | `` | `` |
| 11 | `BK_ADR2` | `char(40)` | YES |  |  | `` | `` |
| 12 | `DESC1` | `char(60)` | YES |  |  | `` | `` |
| 13 | `DESC2` | `char(60)` | YES |  |  | `` | `` |
| 14 | `Id` | `int` | NO | YES | YES | `` | `` |

## 45. `[dbo].[pbl_trs]`

- Rows: `16703`
- Columns: `16`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `VEND_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `INVS_NUM` | `char(10)` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 4 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 5 | `INVS_TM` | `int` | YES |  |  | `` | `` |
| 6 | `CHK_NUM` | `int` | YES |  |  | `` | `` |
| 7 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 8 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 9 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 10 | `ACT_NUM` | `tinyint` | YES |  |  | `` | `` |
| 11 | `MEMO_LN` | `char(20)` | YES |  |  | `` | `` |
| 12 | `PAID_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `NOTE_NUM` | `char(10)` | YES |  |  | `` | `` |
| 14 | `OPEN_NUM` | `char(8)` | YES |  |  | `` | `` |
| 15 | `INS_VAL` | `tinyint` | YES |  |  | `` | `` |
| 16 | `CRD_INVS` | `char(10)` | YES |  |  | `` | `` |

## 46. `[dbo].[inv]`

- Rows: `16547`
- Columns: `137`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PROD_CD` | `char(21)` | NO |  |  | `` | `` |
| 2 | `DESCRIP` | `char(61)` | YES |  |  | `` | `` |
| 3 | `DESCRIP1` | `char(60)` | YES |  |  | `` | `` |
| 4 | `DESCRIP2` | `char(60)` | YES |  |  | `` | `` |
| 5 | `UNIT_NM` | `char(4)` | YES |  |  | `` | `` |
| 6 | `ORDERSIZE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 7 | `MINSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `RETAIL_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `WHOLE_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `WHOLE_PRS2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `WHOLE_PRS3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `CORP_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `PRICE_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `PRICE_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `PRICE_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 16 | `PRICE_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `PRICE_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `PRICE_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `RG_X` | `char(1)` | YES |  |  | `` | `` |
| 20 | `RG_0` | `decimal(8,0)` | YES |  |  | `` | `` |
| 21 | `RG_1` | `decimal(8,0)` | YES |  |  | `` | `` |
| 22 | `RG_2` | `decimal(8,0)` | YES |  |  | `` | `` |
| 23 | `RG_3` | `decimal(8,0)` | YES |  |  | `` | `` |
| 24 | `RG_4` | `decimal(8,0)` | YES |  |  | `` | `` |
| 25 | `RG_5` | `decimal(8,0)` | YES |  |  | `` | `` |
| 26 | `RG_6` | `decimal(8,0)` | YES |  |  | `` | `` |
| 27 | `CREATE_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 28 | `NT_1` | `char(70)` | YES |  |  | `` | `` |
| 29 | `NT_2` | `char(70)` | YES |  |  | `` | `` |
| 30 | `INV_LOCT` | `char(21)` | YES |  |  | `` | `` |
| 31 | `PROD_YR` | `char(12)` | YES |  |  | `` | `` |
| 32 | `RELEASE_FLAG` | `char(1)` | YES |  |  | `` | `` |
| 33 | `COMP_ITEM` | `char(1)` | YES |  |  | `` | `` |
| 34 | `CLASS_CD` | `char(30)` | YES |  |  | `` | `` |
| 35 | `CAT_CD` | `char(8)` | YES |  |  | `` | `` |
| 36 | `VEND_ID` | `char(11)` | YES |  |  | `` | `` |
| 37 | `VEND_PROD` | `char(26)` | YES |  |  | `` | `` |
| 38 | `PC_CASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `BOX_CASE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 40 | `CASE_SF` | `decimal(21,6)` | YES |  |  | `` | `` |
| 41 | `UNIT_SF` | `decimal(21,6)` | YES |  |  | `` | `` |
| 42 | `SALES_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 43 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 44 | `COMM_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 45 | `PROM_IND` | `char(1)` | YES |  |  | `` | `` |
| 46 | `PROM_EXP` | `decimal(8,0)` | YES |  |  | `` | `` |
| 47 | `TAX_IND` | `char(1)` | YES |  |  | `` | `` |
| 48 | `STK_IND` | `char(1)` | YES |  |  | `` | `` |
| 49 | `UPC_CD` | `char(14)` | YES |  |  | `` | `` |
| 50 | `CHT_NUM` | `decimal(8,0)` | YES |  |  | `` | `` |
| 51 | `CHT_NUM_2` | `decimal(8,0)` | YES |  |  | `` | `` |
| 52 | `UPDT_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 53 | `UPDT_BY` | `char(10)` | YES |  |  | `` | `` |
| 54 | `DEPT_NUM` | `char(30)` | YES |  |  | `` | `` |
| 55 | `CAT_NUM` | `char(30)` | YES |  |  | `` | `` |
| 56 | `CAT_PAGE` | `char(20)` | YES |  |  | `` | `` |
| 57 | `CASE_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 58 | `UT_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 59 | `SO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 60 | `PO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 61 | `WT_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 62 | `PK_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 63 | `WIP_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 64 | `RMA_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 65 | `PRS_TYPE` | `char(1)` | YES |  |  | `` | `` |
| 66 | `OEM` | `char(20)` | YES |  |  | `` | `` |
| 67 | `ALT_CD` | `char(20)` | YES |  |  | `` | `` |
| 68 | `LEAD_DAY` | `decimal(5,0)` | YES |  |  | `` | `` |
| 69 | `UNIT_COLOR` | `char(10)` | YES |  |  | `` | `` |
| 70 | `UNIT_SIZE` | `char(16)` | YES |  |  | `` | `` |
| 71 | `PHYC_DT` | `decimal(8,0)` | YES |  |  | `` | `` |
| 72 | `LEAD_DAYS` | `decimal(5,0)` | YES |  |  | `` | `` |
| 73 | `DIM_1` | `decimal(21,6)` | YES |  |  | `` | `` |
| 74 | `DIM_2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 75 | `DIM_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 76 | `DEF_UNIT` | `char(2)` | YES |  |  | `` | `` |
| 77 | `IMAGE_NM` | `char(200)` | YES |  |  | `` | `` |
| 78 | `IMAGE_NM2` | `char(200)` | YES |  |  | `` | `` |
| 79 | `COMM_SW` | `char(1)` | YES |  |  | `` | `` |
| 80 | `USE_MAX_SOLD` | `char(1)` | YES |  |  | `` | `` |
| 81 | `MAX_SOLD_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 82 | `MAX_SOLD_DAYS` | `decimal(8,0)` | YES |  |  | `` | `` |
| 83 | `REMARK` | `char(20)` | YES |  |  | `` | `` |
| 84 | `BRD_NM` | `char(20)` | YES |  |  | `` | `` |
| 85 | `MAKER` | `char(40)` | YES |  |  | `` | `` |
| 86 | `MODEL` | `char(40)` | YES |  |  | `` | `` |
| 87 | `YEAR_FM` | `decimal(11,2)` | YES |  |  | `` | `` |
| 88 | `YEAR_TO` | `decimal(11,2)` | YES |  |  | `` | `` |
| 89 | `START_SLS` | `int` | YES |  |  | `` | `` |
| 90 | `STATUS` | `char(10)` | YES |  |  | `` | `` |
| 91 | `CATEGORY` | `char(30)` | YES |  |  | `` | `` |
| 92 | `LENGTH` | `char(30)` | YES |  |  | `` | `` |
| 93 | `WIDTH` | `char(30)` | YES |  |  | `` | `` |
| 94 | `HEIGHT` | `char(30)` | YES |  |  | `` | `` |
| 95 | `DEF_COST` | `decimal(21,6)` | YES |  |  | `` | `` |
| 96 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 97 | `NAPA` | `char(1)` | YES |  |  | `` | `` |
| 98 | `DEF_WHS` | `char(4)` | YES |  |  | `` | `` |
| 99 | `RELT_SW` | `char(1)` | YES |  |  | `` | `` |
| 100 | `RELT_ITEM` | `char(20)` | YES |  |  | `` | `` |
| 101 | `MFR_NM` | `char(30)` | YES |  |  | `` | `` |
| 102 | `RELT_KEY1` | `tinyint` | YES |  |  | `` | `` |
| 103 | `CRV_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 104 | `F_1` | `char(20)` | YES |  |  | `` | `` |
| 105 | `GROUP_CD` | `char(30)` | YES |  |  | `` | `` |
| 106 | `SUBGROUP_CD` | `char(30)` | YES |  |  | `` | `` |
| 107 | `SHIP_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 108 | `EXPRESS_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 109 | `INTL_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 110 | `INV_TYPE` | `char(8)` | YES |  |  | `` | `` |
| 111 | `WO_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 112 | `QTY_BATCH` | `decimal(21,6)` | YES |  |  | `` | `` |
| 113 | `QTY_BATCH2` | `decimal(21,6)` | YES |  |  | `` | `` |
| 114 | `QTY_BATCH3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 115 | `UPC_CD2` | `char(20)` | YES |  |  | `` | `` |
| 116 | `DESCRIP3` | `char(60)` | YES |  |  | `` | `` |
| 117 | `BOM_CD` | `char(20)` | YES |  |  | `` | `` |
| 118 | `RSV_1` | `char(60)` | YES |  |  | `` | `` |
| 119 | `RSV_2` | `char(60)` | YES |  |  | `` | `` |
| 120 | `RSV_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 121 | `RSV_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 122 | `RSV_5` | `int` | YES |  |  | `` | `` |
| 123 | `RSV_6` | `int` | YES |  |  | `` | `` |
| 124 | `STYLE_CD` | `char(20)` | YES |  |  | `` | `` |
| 125 | `BRAND_CD` | `char(20)` | YES |  |  | `` | `` |
| 126 | `SEASONS` | `char(20)` | YES |  |  | `` | `` |
| 127 | `MISC_CD` | `char(20)` | YES |  |  | `` | `` |
| 128 | `MANUFACTURE_CD` | `char(20)` | YES |  |  | `` | `` |
| 129 | `MODEL_CD` | `char(20)` | YES |  |  | `` | `` |
| 130 | `MADEIN` | `char(40)` | YES |  |  | `` | `` |
| 131 | `MATERIAL1` | `char(40)` | YES |  |  | `` | `` |
| 132 | `MATERIAL2` | `char(40)` | YES |  |  | `` | `` |
| 133 | `MATERIAL3` | `char(40)` | YES |  |  | `` | `` |
| 134 | `MATERIAL4` | `char(40)` | YES |  |  | `` | `` |
| 135 | `MATERIAL5` | `char(40)` | YES |  |  | `` | `` |
| 136 | `MAXSTOCK` | `decimal(21,6)` | YES |  |  | `` | `` |
| 137 | `Id` | `int` | NO | YES | YES | `` | `` |

## 47. `[dbo].[pbl_ins]`

- Rows: `15994`
- Columns: `20`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `VEND_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `INVS_NUM` | `char(10)` | NO |  |  | `` | `` |
| 3 | `PO_NUM` | `char(20)` | YES |  |  | `` | `` |
| 4 | `INVS_DT` | `int` | NO |  |  | `` | `` |
| 5 | `INVS_TM` | `int` | YES |  |  | `` | `` |
| 6 | `VEN_INVS_DT` | `int` | YES |  |  | `` | `` |
| 7 | `CHT_NUM` | `int` | YES |  |  | `` | `` |
| 8 | `GL_ACT` | `char(25)` | YES |  |  | `` | `` |
| 9 | `DUE_DT` | `int` | YES |  |  | `` | `` |
| 10 | `REFER_NUM` | `char(18)` | YES |  |  | `` | `` |
| 11 | `NOTE_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `INVS_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `DISCNT_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 14 | `BAL_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `OPEN_NUM` | `char(10)` | YES |  |  | `` | `` |
| 16 | `AP_PT` | `smallint` | YES |  |  | `` | `` |
| 17 | `INS_VAL` | `tinyint` | YES |  |  | `` | `` |
| 18 | `LAST_UPDT` | `int` | YES |  |  | `` | `` |
| 19 | `LAST_OPEN` | `char(10)` | YES |  |  | `` | `` |
| 20 | `PROJ_NUM` | `char(25)` | YES |  |  | `` | `` |

## 48. `[dbo].[bnk_pmt]`

- Rows: `14307`
- Columns: `18`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BANK_NUM` | `tinyint` | YES |  |  | `` | `` |
| 2 | `CHK_NUM` | `decimal(21,3)` | YES |  |  | `` | `` |
| 3 | `CHK_DT` | `int` | YES |  |  | `` | `` |
| 4 | `TRS_DT` | `int` | YES |  |  | `` | `` |
| 5 | `TRS_TM` | `int` | YES |  |  | `` | `` |
| 6 | `PAYEE` | `char(40)` | YES |  |  | `` | `` |
| 7 | `PMT_MEMO` | `char(40)` | YES |  |  | `` | `` |
| 8 | `DBT_ACT` | `char(25)` | YES |  |  | `` | `` |
| 9 | `CRD_ACT` | `char(25)` | YES |  |  | `` | `` |
| 10 | `OPERATOR` | `char(10)` | YES |  |  | `` | `` |
| 11 | `REF_NUM` | `char(10)` | YES |  |  | `` | `` |
| 12 | `PAID_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 14 | `TRS_NUM` | `int` | NO |  |  | `` | `` |
| 15 | `TRS_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 16 | `CHK_DT1` | `char(10)` | YES |  |  | `` | `` |
| 17 | `TRS_DT1` | `char(10)` | YES |  |  | `` | `` |
| 18 | `TRS_TM1` | `char(12)` | YES |  |  | `` | `` |

## 49. `[dbo].[bol_log]`

- Rows: `11259`
- Columns: `19`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BLG_DT` | `int` | YES |  |  | `` | `` |
| 2 | `BLG_TIME` | `int` | YES |  |  | `` | `` |
| 3 | `COMM_LN` | `smallint` | NO |  |  | `` | `` |
| 4 | `SHIP_NUM` | `int` | NO |  |  | `` | `` |
| 5 | `SHIP_CD` | `tinyint` | NO |  |  | `` | `` |
| 6 | `INVS_CD` | `char(1)` | NO |  |  | `` | `` |
| 7 | `BOX_NUM` | `char(60)` | YES |  |  | `` | `` |
| 8 | `DESC` | `char(60)` | YES |  |  | `` | `` |
| 9 | `PRICE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `WEIGHT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `RATE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `CHARGE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 13 | `CLASS` | `char(60)` | YES |  |  | `` | `` |
| 14 | `COD_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 15 | `COD_MTD` | `char(1)` | YES |  |  | `` | `` |
| 16 | `COD_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `PAIRS` | `int` | YES |  |  | `` | `` |
| 18 | `FRT_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `QTY` | `decimal(21,6)` | YES |  |  | `` | `` |

## 50. `[dbo].[dvf_chg]`

- Rows: `9269`
- Columns: `5`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `UPS_CD` | `tinyint` | NO |  |  | `` | `` |
| 2 | `UPS_ZONE` | `smallint` | NO |  |  | `` | `` |
| 3 | `WT_TO` | `smallint` | NO |  |  | `` | `` |
| 4 | `UPS_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 5 | `UPS_FEE2` | `decimal(21,6)` | YES |  |  | `` | `` |

## 51. `[dbo].[custdesc]`

- Rows: `6747`
- Columns: `33`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `CUS_ID` | `char(10)` | NO |  |  | `` | `` |
| 2 | `TYPE_CD` | `decimal(5,0)` | YES |  |  | `` | `` |
| 3 | `UT_DESC1` | `char(255)` | YES |  |  | `` | `` |
| 4 | `UT_DESC2` | `char(255)` | YES |  |  | `` | `` |
| 5 | `UT_DESC3` | `char(255)` | YES |  |  | `` | `` |
| 6 | `UT_DESC4` | `char(255)` | YES |  |  | `` | `` |
| 7 | `UT_DESC5` | `char(255)` | YES |  |  | `` | `` |
| 8 | `UT_DESC6` | `char(255)` | YES |  |  | `` | `` |
| 9 | `UT_DESC7` | `char(255)` | YES |  |  | `` | `` |
| 10 | `UT_DESC8` | `char(255)` | YES |  |  | `` | `` |
| 11 | `UT_DESC9` | `char(255)` | YES |  |  | `` | `` |
| 12 | `UT_DESC10` | `char(255)` | YES |  |  | `` | `` |
| 13 | `UT_DESC11` | `char(255)` | YES |  |  | `` | `` |
| 14 | `UT_DESC12` | `char(255)` | YES |  |  | `` | `` |
| 15 | `UT_DESC13` | `char(255)` | YES |  |  | `` | `` |
| 16 | `UT_DESC14` | `char(255)` | YES |  |  | `` | `` |
| 17 | `UT_DESC15` | `char(255)` | YES |  |  | `` | `` |
| 18 | `UT_DESC16` | `char(255)` | YES |  |  | `` | `` |
| 19 | `UT_DESC17` | `char(255)` | YES |  |  | `` | `` |
| 20 | `UT_DESC18` | `char(255)` | YES |  |  | `` | `` |
| 21 | `UT_DESC19` | `char(255)` | YES |  |  | `` | `` |
| 22 | `UT_DESC20` | `char(255)` | YES |  |  | `` | `` |
| 23 | `UPS_ACT` | `char(25)` | YES |  |  | `` | `` |
| 24 | `RSV_1` | `char(255)` | YES |  |  | `` | `` |
| 25 | `RSV_2` | `char(255)` | YES |  |  | `` | `` |
| 26 | `RSV_3` | `char(255)` | YES |  |  | `` | `` |
| 27 | `RSV_4` | `char(255)` | YES |  |  | `` | `` |
| 28 | `RSV_5` | `char(255)` | YES |  |  | `` | `` |
| 29 | `RSV_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `RSV_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `RSV_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 32 | `RSV_9` | `decimal(21,6)` | YES |  |  | `` | `` |
| 33 | `RSV_10` | `decimal(21,6)` | YES |  |  | `` | `` |

## 52. `[dbo].[qtn_log]`

- Rows: `6549`
- Columns: `24`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `QLG_DT` | `int` | YES |  |  | `` | `` |
| 2 | `QLG_TIME` | `int` | YES |  |  | `` | `` |
| 3 | `QTN_NUM` | `int` | NO |  |  | `` | `` |
| 4 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 5 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 6 | `PROD_CD` | `char(21)` | YES |  |  | `` | `` |
| 7 | `QTN_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `UNIT_PRS` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `QTN_LNT` | `char(1)` | YES |  |  | `` | `` |
| 10 | `LINE_CD` | `tinyint` | YES |  |  | `` | `` |
| 11 | `LINE_TX` | `char(1)` | YES |  |  | `` | `` |
| 12 | `NT_NUM` | `smallint` | YES |  |  | `` | `` |
| 13 | `PROD_COMP` | `char(1)` | YES |  |  | `` | `` |
| 14 | `UT_DESC` | `char(60)` | YES |  |  | `` | `` |
| 15 | `COMM_LN` | `smallint` | NO |  |  | `` | `` |
| 16 | `ETA_DT` | `int` | YES |  |  | `` | `` |
| 17 | `WHS_NUM` | `char(8)` | YES |  |  | `` | `` |
| 18 | `PC_UNIT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `DEF_UT` | `char(2)` | YES |  |  | `` | `` |
| 20 | `REF_NUM` | `char(15)` | YES |  |  | `` | `` |
| 21 | `RSV_1` | `char(20)` | YES |  |  | `` | `` |
| 22 | `RSV_2` | `char(20)` | YES |  |  | `` | `` |
| 23 | `RSV_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `RSV_4` | `decimal(21,6)` | YES |  |  | `` | `` |

## 53. `[dbo].[chk_note]`

- Rows: `6515`
- Columns: `9`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `ACT_NUM` | `tinyint` | NO |  |  | `` | `` |
| 2 | `CHK_NUM` | `decimal(21,3)` | NO |  |  | `` | `` |
| 3 | `CHK_DT` | `int` | YES |  |  | `` | `` |
| 4 | `CHK_BY` | `char(10)` | YES |  |  | `` | `` |
| 5 | `MEMO_LN` | `char(40)` | YES |  |  | `` | `` |
| 6 | `NOTE_TX` | `char(220)` | YES |  |  | `` | `` |
| 7 | `INS_VAL` | `tinyint` | YES |  |  | `` | `` |
| 8 | `PAYEE` | `char(40)` | YES |  |  | `` | `` |
| 9 | `CHK_DT1` | `char(10)` | YES |  |  | `` | `` |

## 54. `[dbo].[poshpf]`

- Rows: `5340`
- Columns: `44`
- Primary key: `PK_NUM`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PK_NUM` | `int` | NO |  | YES | `` | `` |
| 2 | `PUR_NUM` | `char(20)` | NO |  |  | `` | `` |
| 3 | `PUR_CD` | `int` | NO |  |  | `` | `` |
| 4 | `BAT_NUM` | `int` | NO |  |  | `` | `` |
| 5 | `ETA_SHP_DT` | `int` | YES |  |  | `` | `` |
| 6 | `ETA_ARV_DT` | `int` | YES |  |  | `` | `` |
| 7 | `SHP_DT` | `int` | YES |  |  | `` | `` |
| 8 | `ETA_DPT_DT` | `int` | YES |  |  | `` | `` |
| 9 | `BL_NUM` | `char(20)` | YES |  |  | `` | `` |
| 10 | `VSL_NM` | `char(60)` | YES |  |  | `` | `` |
| 11 | `CARRIER_NM` | `char(60)` | YES |  |  | `` | `` |
| 12 | `PORT_ID` | `char(20)` | YES |  |  | `` | `` |
| 13 | `CUS_ENTRY` | `char(60)` | NO |  |  | `` | `` |
| 14 | `RSV_1` | `char(60)` | YES |  |  | `` | `` |
| 15 | `RSV_2` | `char(60)` | YES |  |  | `` | `` |
| 16 | `RSV_3` | `decimal(21,6)` | YES |  |  | `` | `` |
| 17 | `RSV_4` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `PSF_DT` | `int` | NO |  |  | `` | `` |
| 19 | `ORIGEN` | `char(20)` | YES |  |  | `` | `` |
| 20 | `VEN_ID` | `char(10)` | NO |  |  | `` | `` |
| 21 | `CUS_ID` | `char(10)` | YES |  |  | `` | `` |
| 22 | `STATUS_CD` | `char(20)` | YES |  |  | `` | `` |
| 23 | `NOTE` | `char(200)` | YES |  |  | `` | `` |
| 24 | `CREATE_DT` | `int` | YES |  |  | `` | `` |
| 25 | `CREATE_TM` | `int` | YES |  |  | `` | `` |
| 26 | `CREATE_BY` | `char(10)` | YES |  |  | `` | `` |
| 27 | `UPDATE_DT` | `int` | YES |  |  | `` | `` |
| 28 | `UPDATE_TM` | `int` | YES |  |  | `` | `` |
| 29 | `UPDATE_BY` | `char(10)` | YES |  |  | `` | `` |
| 30 | `ARV_DT` | `int` | YES |  |  | `` | `` |
| 31 | `LOAD_PORT` | `char(20)` | YES |  |  | `` | `` |
| 32 | `SHIP_TYPE` | `char(20)` | YES |  |  | `` | `` |
| 33 | `OCEAN_LINE` | `char(20)` | YES |  |  | `` | `` |
| 34 | `OCEAN_FREIGHT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 35 | `LC_NUM` | `char(20)` | YES |  |  | `` | `` |
| 36 | `DP_LOAN` | `char(20)` | YES |  |  | `` | `` |
| 37 | `CLERAN_CUST` | `char(20)` | YES |  |  | `` | `` |
| 38 | `TMF` | `char(20)` | YES |  |  | `` | `` |
| 39 | `PORT_CHECK` | `char(20)` | YES |  |  | `` | `` |
| 40 | `DELIVERY_ORD` | `char(20)` | YES |  |  | `` | `` |
| 41 | `LAST_FREE_DT` | `int` | YES |  |  | `` | `` |
| 42 | `FIRM_DELIV_DT` | `int` | YES |  |  | `` | `` |
| 43 | `CHK10_2` | `tinyint` | YES |  |  | `` | `` |
| 44 | `LACEY_ACT` | `tinyint` | YES |  |  | `` | `` |

## 55. `[dbo].[acctpbl]`

- Rows: `5337`
- Columns: `34`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `VEND_ID` | `char(11)` | NO |  |  | `` | `` |
| 2 | `INVS_NUM` | `char(10)` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 4 | `PORD_NUM` | `char(8)` | YES |  |  | `` | `` |
| 5 | `BAT_NUM` | `int` | YES |  |  | `` | `` |
| 6 | `RCV_DT` | `int` | YES |  |  | `` | `` |
| 7 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 8 | `INVS_TM` | `int` | YES |  |  | `` | `` |
| 9 | `OPEN_NUM` | `char(8)` | YES |  |  | `` | `` |
| 10 | `BUS_CD` | `int` | YES |  |  | `` | `` |
| 11 | `SHIP_CD` | `int` | YES |  |  | `` | `` |
| 12 | `HANDL_CD` | `int` | YES |  |  | `` | `` |
| 13 | `MISC_CD` | `int` | YES |  |  | `` | `` |
| 14 | `TAX_CD` | `int` | YES |  |  | `` | `` |
| 15 | `DISC_CD` | `int` | YES |  |  | `` | `` |
| 16 | `DUE_DT` | `int` | YES |  |  | `` | `` |
| 17 | `INVS_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 18 | `INVS_TAX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 19 | `MISC_CHG` | `decimal(21,6)` | YES |  |  | `` | `` |
| 20 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 21 | `SHIP_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 22 | `DISCNT_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 23 | `DISCNT_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 24 | `REFER_NUM` | `char(10)` | YES |  |  | `` | `` |
| 25 | `VEN_INVS_DT` | `int` | YES |  |  | `` | `` |
| 26 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 27 | `CALC_SEL` | `tinyint` | YES |  |  | `` | `` |
| 28 | `CONT_NUM` | `char(20)` | YES |  |  | `` | `` |
| 29 | `CONT_TYPE` | `tinyint` | YES |  |  | `` | `` |
| 30 | `CONT_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `CONT_WT` | `int` | YES |  |  | `` | `` |
| 32 | `CONT_VOL` | `int` | YES |  |  | `` | `` |
| 33 | `LAST_UPDT` | `int` | YES |  |  | `` | `` |
| 34 | `LAST_OPEN` | `char(11)` | YES |  |  | `` | `` |

## 56. `[dbo].[pur_ord]`

- Rows: `5283`
- Columns: `69`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `PUR_DT` | `int` | NO |  |  | `` | `` |
| 2 | `PUR_NUM` | `char(8)` | NO |  |  | `` | `` |
| 3 | `VEN_ID` | `char(11)` | NO |  |  | `` | `` |
| 4 | `SP_CD` | `tinyint` | YES |  |  | `` | `` |
| 5 | `TERM` | `tinyint` | YES |  |  | `` | `` |
| 6 | `SALES_NUM` | `char(10)` | YES |  |  | `` | `` |
| 7 | `DISCOUNT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `PUR_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `PUR_TAX` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `PAID_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `PAID_BY` | `tinyint` | YES |  |  | `` | `` |
| 12 | `NT_SEL` | `char(1)` | YES |  |  | `` | `` |
| 13 | `PUR_ADR1` | `char(60)` | YES |  |  | `` | `` |
| 14 | `PUR_ADR2` | `char(60)` | YES |  |  | `` | `` |
| 15 | `PUR_ADR22` | `char(60)` | YES |  |  | `` | `` |
| 16 | `PUR_ADR3` | `char(60)` | YES |  |  | `` | `` |
| 17 | `PUR_COUNTRY` | `char(50)` | YES |  |  | `` | `` |
| 18 | `NOTE_NUM` | `int` | YES |  |  | `` | `` |
| 19 | `EST_DT` | `int` | YES |  |  | `` | `` |
| 20 | `SHIP_DESC` | `char(25)` | YES |  |  | `` | `` |
| 21 | `WHS_NUM` | `char(6)` | YES |  |  | `` | `` |
| 22 | `TERM_DESC` | `char(15)` | YES |  |  | `` | `` |
| 23 | `TERMS_DAY` | `smallint` | YES |  |  | `` | `` |
| 24 | `TERMS_COD` | `char(1)` | YES |  |  | `` | `` |
| 25 | `FOB_DESC` | `char(25)` | YES |  |  | `` | `` |
| 26 | `PTERM_DESC` | `char(20)` | YES |  |  | `` | `` |
| 27 | `CUT_OFF_DT` | `int` | YES |  |  | `` | `` |
| 28 | `ONBD_DT` | `int` | YES |  |  | `` | `` |
| 29 | `WT_DT` | `int` | YES |  |  | `` | `` |
| 30 | `PUR_DIM` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `PUR_CASE` | `int` | YES |  |  | `` | `` |
| 32 | `ATTN` | `char(30)` | YES |  |  | `` | `` |
| 33 | `DEF_PRS` | `tinyint` | YES |  |  | `` | `` |
| 34 | `CUS_ID` | `char(11)` | YES |  |  | `` | `` |
| 35 | `PUR_WT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 36 | `PUR_QB` | `decimal(21,6)` | YES |  |  | `` | `` |
| 37 | `CURRENCY` | `char(20)` | YES |  |  | `` | `` |
| 38 | `EXCHANGE_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 39 | `ORD_NUM` | `char(20)` | YES |  |  | `` | `` |
| 40 | `REF_NUM` | `char(30)` | YES |  |  | `` | `` |
| 41 | `CONT_NUM` | `char(30)` | YES |  |  | `` | `` |
| 42 | `TYPE_CD` | `char(6)` | YES |  |  | `` | `` |
| 43 | `SHIP_DT` | `int` | YES |  |  | `` | `` |
| 44 | `CAN_DT` | `int` | YES |  |  | `` | `` |
| 45 | `PACK_DT` | `int` | YES |  |  | `` | `` |
| 46 | `RESV_1` | `char(20)` | YES |  |  | `` | `` |
| 47 | `RESV_2` | `decimal(21,3)` | YES |  |  | `` | `` |
| 48 | `MFG_CFM_PO` | `char(20)` | YES |  |  | `` | `` |
| 49 | `SCH_PACK_DT` | `int` | YES |  |  | `` | `` |
| 50 | `Id` | `int` | NO | YES | YES | `` | `` |
| 51 | `MGR_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 52 | `MGR_PROV_DT` | `int` | YES |  |  | `` | `` |
| 53 | `ASM_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 54 | `ASM_PROV_DT` | `int` | YES |  |  | `` | `` |
| 55 | `INV_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 56 | `INV_PROV_DT` | `int` | YES |  |  | `` | `` |
| 57 | `MISC_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 58 | `MISC_PROV_DT` | `int` | YES |  |  | `` | `` |
| 59 | `QC_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 60 | `QC_PROV_DT` | `int` | YES |  |  | `` | `` |
| 61 | `TS_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 62 | `TS_PROV_DT` | `int` | YES |  |  | `` | `` |
| 63 | `ACT_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 64 | `ACT_PROV_DT` | `int` | YES |  |  | `` | `` |
| 65 | `SLS_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 66 | `SLS_PROV_DT` | `int` | YES |  |  | `` | `` |
| 67 | `RMA_PROV_BY` | `char(8)` | YES |  |  | `` | `` |
| 68 | `RMA_PROV_DT` | `int` | YES |  |  | `` | `` |
| 69 | `STATUS` | `char(20)` | YES |  |  | `` | `` |

## 57. `[dbo].[bnk_cltr]`

- Rows: `4014`
- Columns: `13`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `TYPE_CD` | `int` | NO |  |  | `` | `` |
| 2 | `BANK_NUM` | `int` | NO |  |  | `` | `` |
| 3 | `TRS_NUM` | `int` | YES |  |  | `` | `` |
| 4 | `STM_DT` | `int` | YES |  |  | `` | `` |
| 5 | `CUS_ID` | `char(12)` | YES |  |  | `` | `` |
| 6 | `CHK_NUM` | `char(30)` | NO |  |  | `` | `` |
| 7 | `CHK_CD` | `int` | YES |  |  | `` | `` |
| 8 | `CHK_AMT` | `decimal(19,3)` | YES |  |  | `` | `` |
| 9 | `STATUS_CD` | `tinyint` | YES |  |  | `` | `` |
| 10 | `INVS_DT` | `int` | YES |  |  | `` | `` |
| 11 | `INVS_NUM` | `int` | YES |  |  | `` | `` |
| 12 | `INVS_CD` | `int` | YES |  |  | `` | `` |
| 13 | `TRS_TYPE` | `int` | YES |  |  | `` | `` |

## 58. `[dbo].[exc_whs]`

- Rows: `3721`
- Columns: `32`
- Primary key: `ID`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `BAT_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `BAT_DT` | `int` | YES |  |  | `` | `` |
| 3 | `BAT_TM` | `int` | YES |  |  | `` | `` |
| 4 | `PROCESSOR` | `char(10)` | YES |  |  | `` | `` |
| 5 | `BAT_NT1` | `char(70)` | YES |  |  | `` | `` |
| 6 | `BAT_NT2` | `char(70)` | YES |  |  | `` | `` |
| 7 | `BAT_QTY` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `BAT_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 9 | `SHIP_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 10 | `HANDL_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 11 | `MISC_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 12 | `FM_ADDR1` | `char(60)` | YES |  |  | `` | `` |
| 13 | `FM_ADDR2` | `char(60)` | YES |  |  | `` | `` |
| 14 | `FM_CITY` | `char(40)` | YES |  |  | `` | `` |
| 15 | `FM_ST` | `char(40)` | YES |  |  | `` | `` |
| 16 | `FM_ZIP` | `char(10)` | YES |  |  | `` | `` |
| 17 | `FM_COUNTRY` | `char(40)` | YES |  |  | `` | `` |
| 18 | `TO_ADDR1` | `char(60)` | YES |  |  | `` | `` |
| 19 | `TO_ADDR2` | `char(60)` | YES |  |  | `` | `` |
| 20 | `TO_CITY` | `char(40)` | YES |  |  | `` | `` |
| 21 | `TO_ST` | `char(40)` | YES |  |  | `` | `` |
| 22 | `TO_ZIP` | `char(10)` | YES |  |  | `` | `` |
| 23 | `TO_COUNTRY` | `char(40)` | YES |  |  | `` | `` |
| 24 | `RSV_1` | `char(40)` | YES |  |  | `` | `` |
| 25 | `RSV_2` | `char(40)` | YES |  |  | `` | `` |
| 26 | `RSV_3` | `char(40)` | YES |  |  | `` | `` |
| 27 | `RSV_4` | `char(40)` | YES |  |  | `` | `` |
| 28 | `RSV_5` | `decimal(21,6)` | YES |  |  | `` | `` |
| 29 | `RSV_6` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `RSV_7` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `RSV_8` | `decimal(21,6)` | YES |  |  | `` | `` |
| 32 | `ID` | `int` | NO | YES | YES | `` | `` |

## 59. `[dbo].[invs_lnt]`

- Rows: `2758`
- Columns: `5`
- Primary key: `Id`

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `INVS_NUM` | `int` | NO |  |  | `` | `` |
| 2 | `INVS_CD` | `tinyint` | NO |  |  | `` | `` |
| 3 | `NT_NUM` | `smallint` | NO |  |  | `` | `` |
| 4 | `INVS_NT` | `char(600)` | YES |  |  | `` | `` |
| 5 | `Id` | `int` | NO | YES | YES | `` | `` |

## 60. `[dbo].[shp_ld]`

- Rows: `2118`
- Columns: `45`
- Primary key: not found in metadata

| # | Column | Type | Nullable | Identity | Primary Key | Default | Computed |
|---:|---|---|---|---|---|---|---|
| 1 | `SHIP_NUM` | `char(10)` | NO |  |  | `` | `` |
| 2 | `SHIP_CD` | `tinyint` | NO |  |  | `` | `` |
| 3 | `INVS_CD` | `char(1)` | NO |  |  | `` | `` |
| 4 | `WHS_NUM` | `char(10)` | YES |  |  | `` | `` |
| 5 | `TRK_NUM` | `char(25)` | YES |  |  | `` | `` |
| 6 | `SHIP_DESC` | `char(30)` | YES |  |  | `` | `` |
| 7 | `VOL_FT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 8 | `CAR_NM` | `char(30)` | YES |  |  | `` | `` |
| 9 | `SHP_FM` | `char(30)` | YES |  |  | `` | `` |
| 10 | `SHP_ADR` | `char(40)` | YES |  |  | `` | `` |
| 11 | `SHP_ADR2` | `char(40)` | YES |  |  | `` | `` |
| 12 | `SHP_ADR22` | `char(40)` | YES |  |  | `` | `` |
| 13 | `SHP_ADR3` | `char(40)` | YES |  |  | `` | `` |
| 14 | `SHP_ZIP` | `char(10)` | YES |  |  | `` | `` |
| 15 | `INS_ADR` | `char(40)` | YES |  |  | `` | `` |
| 16 | `INS_ADR2` | `char(40)` | YES |  |  | `` | `` |
| 17 | `INS_ADR22` | `char(40)` | YES |  |  | `` | `` |
| 18 | `INS_ADR3` | `char(40)` | YES |  |  | `` | `` |
| 19 | `INS_ZIP` | `char(10)` | YES |  |  | `` | `` |
| 20 | `BILL_ADR` | `char(40)` | YES |  |  | `` | `` |
| 21 | `BILL_ADR2` | `char(40)` | YES |  |  | `` | `` |
| 22 | `BILL_ADR22` | `char(40)` | YES |  |  | `` | `` |
| 23 | `BILL_ADR3` | `char(40)` | YES |  |  | `` | `` |
| 24 | `BILL_ZIP` | `char(10)` | YES |  |  | `` | `` |
| 25 | `COD_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 26 | `COD_FEE` | `decimal(21,6)` | YES |  |  | `` | `` |
| 27 | `PRE_COL` | `char(1)` | YES |  |  | `` | `` |
| 28 | `INVS_WT` | `int` | YES |  |  | `` | `` |
| 29 | `WT_RT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 30 | `SHIP_AMT` | `decimal(21,6)` | YES |  |  | `` | `` |
| 31 | `SCAC` | `char(20)` | YES |  |  | `` | `` |
| 32 | `ROUTE` | `char(20)` | YES |  |  | `` | `` |
| 33 | `PO_NUM` | `char(12)` | YES |  |  | `` | `` |
| 34 | `SHIP_DT` | `int` | YES |  |  | `` | `` |
| 35 | `SHIP_TM` | `int` | YES |  |  | `` | `` |
| 36 | `SHP_FLAG` | `tinyint` | YES |  |  | `` | `` |
| 37 | `CAR_ADR` | `char(40)` | YES |  |  | `` | `` |
| 38 | `CAR_PHN` | `char(20)` | YES |  |  | `` | `` |
| 39 | `INS_ATTN` | `char(30)` | YES |  |  | `` | `` |
| 40 | `INS_PHN` | `char(20)` | YES |  |  | `` | `` |
| 41 | `SHP_PHN` | `char(20)` | YES |  |  | `` | `` |
| 42 | `SHPF_ADR` | `char(40)` | YES |  |  | `` | `` |
| 43 | `SHPF_ADR2` | `char(40)` | YES |  |  | `` | `` |
| 44 | `SHPF_ADR22` | `char(40)` | YES |  |  | `` | `` |
| 45 | `SHPF_ADR3` | `char(40)` | YES |  |  | `` | `` |
