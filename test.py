
a="FID,FSET_CODE,FCODE,FNAME,FALIAS,FNAME_ENG,FPRODUCT_TYPE,FMANAGER,FCUSTODIAN,FENTRUSTOR,FTRUSTEE,FACCOUNT_MANAGER,FOUTSIDE_TRUSTEE,FPARENT_ID,FCONTRACT_BEG_DATE,FCONTRACT_END_DATE,FFACT_BEG_DATE,FFACT_END_DATE,FORIGIN,FLEAF,FCREATOR_ID,FCREATE_TIME,FLAST_EDITOR_ID,FLAST_EDIT_TIME,FDELETED,FIS_SECURITY,FPRO_TOPTYPE,FOPERATION_UNIT,FCLEARINGMODE,FSTATUS,FPLANLIC_ID,FPORTFOLIO_ID,FMANAGER_CODE,FSWIFT_CODE,FRATE_TYPE,FRATE,FSTART_DATE,FEND_DATE,FACCOUNT_MODE,FORG_NAME,FPROJECT_CODE,FLIQUIDATION_DATE,FPRODUCT_STATUS,FLIQUIDATION_STATUS,FREMARK,FCREATE_ORG,FPENSION_TYPE,FSEARCH_STR,FPRODUCT_RGE_CODE,FPRODUCT_TYPE_CODE,FEDIT_REASON,FDELETE_REASON,FDELETE_USER_ID,FMARK_DELETE_TIME,FREL_ID,FPRO_STATUS,FFIRSTOUTDATE,FFIRSTINDATE,FPLANLICID,FPORTFOLIOID,FSYSNSTATE,FCONTRACT_CODE,FACCMODE,FCHECKED,FCHECKER_ID,FCHECK_TIME,FPAYMENTCATEGORY"

num=0
for i in range(len(a)):
    if a[i] == ',':
        num+=1
print(num)