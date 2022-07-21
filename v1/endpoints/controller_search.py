from optparse import Option
from fastapi import APIRouter
from typing import Dict,List, Optional
from services.search import searchEq, searchGt, searchGe


router_search = APIRouter()

@router_search.get('/search/')
def search(
        table:Optional[str]=None, 
        column:Optional[str]=None, 
        operator:Optional[str]=None,
        value:Optional[str]=None,
        sort_by:Optional[str]=None
    ):
    if(table and column and operator=='eq' and value):
        return searchEq(table,column,value)
    if(table and column and operator=='gt' and value):
        return searchGt(table,column,value)
    if(table and column and operator=='ge' and value):
        return searchGe(table,column,value)

    return {'detail':'nothing to show'}
