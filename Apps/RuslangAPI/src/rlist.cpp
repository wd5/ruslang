#include <cstdlib>
#include "rlist.hpp"

void rList::initArray(unsigned long expectedArraySize)
{
        if(expectedArraySize==0)
        {
            arrayOfObjects=NULL ;
            arraySize=0 ;
        }
        else
        {
            if(expectedArraySize>RLIST_DEVELOPERS_ARRAY_SIZE_LIMIT)
            {
                setResult(failureIndexOverArraySize) ;
                return ;
            }
            arraySize = expectedArraySize ;
            arrayOfObjects = new objectType* [arraySize] ;
        }
}

rList::rList(unsigned long expectedArraySize)
{
        rootOfObjectTree=NULL ;
        //minimumLeaf =NULL;
        //maximumLeaf =NULL ;

        initArray(expectedArraySize) ;
}

rList::~rList()
{
    empty() ;
    if(rootOfObjectTree) delete rootOfObjectTree  ;
    if(arrayOfObjects)delete arrayOfObjects  ;
    arrayOfObjects=NULL ;
    rootOfObjectTree=NULL ;
    //minimumLeaf =NULL;
    //maximumLeaf =NULL ;
    arraySize=0 ;
}

void rList::empty()
{
    
}

bool rList::isEmpty()
{
    return rootOfObjectTree==NULL?true:false ;
}

void rList::add(objectType* obj) 
{
    
}

void rList::add(objectType* obj, rList::index ind) 
{
    if (ind > RLIST_DEVELOPERS_ARRAY_SIZE_LIMIT)
    {
        setResult(failureIndexOverArraySize) ;
        return ;
    }
    if(isEmpty())
    { 
        rootOfObjectTree = new rLeaf(obj) ;
        rootOfObjectTree->ID=ind;
        addToArray(&**rootOfObjectTree,ind) ;
        //minimumLeaf = rootOfObjectTree ;
        //maximumLeaf = rootOfObjectTree ;
        setResult(success) ;
        return ;
    }
    rLeaf* currentLeaf = rootOfObjectTree ;
    
    do
    {
        if(**currentLeaf < *obj)
        {
            if(currentLeaf->rightLeaf)
                currentLeaf = currentLeaf->rightLeaf ;
            else
            {
                currentLeaf->rightLeaf = new rLeaf(obj) ;
                addToArray(obj,ind) ;
                currentLeaf->rightLeaf->ID=ind ;
                setResult(success) ;
                return ;
            }
        }
        else if(**currentLeaf >*obj)
        {
            if(currentLeaf->leftLeaf)
                currentLeaf = currentLeaf->leftLeaf ;
            else
            {
                currentLeaf->leftLeaf = new rLeaf(obj) ;
                addToArray(obj,ind) ;
                currentLeaf->leftLeaf->ID=ind ;
                setResult(success) ;
                return ;
            }
        }
        else
        {   // *current == *obj
            setResult(failureCannotAddObjectAlreadyExists) ;
            return ;
        }
    }
    while(true) ;
    setResult(failureUnknown) ; // we should never exit here with right algorithm
    return ;
}

rList::rLeaf::rLeaf(objectType* obj) 
{
    object=obj ;
    leftLeaf = NULL ;
    rightLeaf = NULL ;
}

rList::rLeaf::~rLeaf() 
{
    // !!! I do not destroy the object itself at the moment
    // do not know if it's right place to do
    delete object ;
}

void rList::addToArray(objectType* obj,rList::index id ) 
{
    if(id>=arraySize)
    {
        if (id > RLIST_DEVELOPERS_ARRAY_SIZE_LIMIT)
        {
            setResult(failureIndexOverArraySize) ;
            return ;
        }
        index newArraySize = sizeof(objectType*)*(id*1.1);
        objectType** newArray=new objectType* [newArraySize] ;
        for( index i;i<newArraySize;i++)
            newArray[i]=NULL ;
        
        for( index i=0; i<arraySize ;i++)
        {
            newArray[i] = arrayOfObjects[i] ;
        }
        if(arrayOfObjects) delete arrayOfObjects ;
        arrayOfObjects=newArray ;
        arraySize = newArraySize ;
    }
    arrayOfObjects[id] = obj ;
    setResult(success) ;
}