/* 
 * File:   rlist.hpp
 * Author: Victor
 *
 * Created on February 13, 2012, 9:52 PM
 * 
 * "Russian language" list
 * List containing words or wordforms
 * Allow quick search of a word/form/ and it's properties by value and quick access by ID ;
 * Accepts allocated and objects, does not manipulate with memory:does not allocate, copy, etc objects in arguments
 * When deletes an object, it uses "delete" to destroy it: object must have proper destructor.
 */

#ifndef RLIST_HPP
#define	RLIST_HPP


typedef int objectType  ;      // "void" will be replaces by Word or WordForm

class rList
{
    typedef unsigned long index ;
private:
    class rLeaf
    {
        friend class rList ;
    private:
        objectType*     object ;
        rLeaf*          leftLeaf ;      // ref to Leaf with Smaller object
                                        // rename to LESS, SMALL???
        rLeaf*          rightLeaf ;     // ref to Leaf with Bigger object
                                        // rename to BIG, BIGGEST???
        index           ID ;
    public:
        rLeaf(objectType*) ;
        ~rLeaf() ;
        objectType& operator*() { return *object; } ;
        
    };
    rLeaf*              rootOfObjectTree ;
    //rLeaf*              minimumLeaf ;
    //rLeaf*              maximumLeaf ;
    
    objectType**        arrayOfObjects ;
    unsigned long       arraySize ;
    /*
     * error code of last operation in the rList instance
     */
    enum resultCodeType
    {
        failureCannotAddAlreadyExists,         // for rList.add()
        failureCannotAddIndexAlreadyExists,      // for rList.add() - index exists
        failureCannotAddObjectAlreadyExists,      // for rList.add() - value exists
        success,
        failureUnknown,
        infoNoActionRequired,
        failureIndexOverArraySize
    } 
        resultCode ;
    
    /*
     */
    void balanceTree() ;
    void setResult(resultCodeType r ) 
        { resultCode=r ;}
    void addToArray(objectType*,rList::index ind );
    void initArray(unsigned long expectedArraySize) ;
    
public:
    rList(unsigned long expectedArraySize=0) ;
    ~rList() ;
    /*
     * 
     */
    /*
     * this add() is used when reading objs from preanalysed/presaved/pre-ID-assigned source
     * add(o,i) and add(o) must be choosen carefuly for not to corrupt data
     */
    void add(objectType* obj, rList::index id) ;
    void add(objectType* obj) ; // auto assign ID
    objectType* operator[](rList::index ind) ;
    objectType* operator[](objectType* obj) ;
    
    void remove(rList::index id) ;
    void empty() ;
    bool isEmpty() ;
};

const unsigned long RLIST_DEVELOPERS_ARRAY_SIZE_LIMIT = 10000000L; // Ten millions

#endif	/* RLIST_HPP */

