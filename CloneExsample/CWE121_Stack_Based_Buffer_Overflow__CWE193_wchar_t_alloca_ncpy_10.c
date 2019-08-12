#include "std_testcase.h"
#ifndef _WIN32
#include <wchar.h>
#endif
#define SRC_STRING L"AAAAAAAAAA"
#ifndef OMITBAD
void CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_10_bad()
{
    wchar_t * data;
    wchar_t * dataBadBuffer = (wchar_t *)ALLOCA((10)*sizeof(wchar_t));
    wchar_t * dataGoodBuffer = (wchar_t *)ALLOCA((10+1)*sizeof(wchar_t));
    if(globalTrue)
    {
        data = dataBadBuffer;
        data[0] = L'\0'; 
    }
    {
        wchar_t source[10+1] = SRC_STRING;
        wcsncpy(data, source, wcslen(source) + 1);
        printWLine(data);
    }
}

#endif

#ifndef OMITGOOD

static void goodG2B1()
{
    wchar_t * data;
    wchar_t * dataBadBuffer = (wchar_t *)ALLOCA((10)*sizeof(wchar_t));
    wchar_t * dataGoodBuffer = (wchar_t *)ALLOCA((10+1)*sizeof(wchar_t));
    if(globalFalse)
    {
        printLine("Benign, fixed string");
    }
    else
    {
        data = dataGoodBuffer;
        data[0] = L'\0'; 
    }
    {
        wchar_t source[10+1] = SRC_STRING;
        wcsncpy(data, source, wcslen(source) + 1);
        printWLine(data);
    }
}

static void goodG2B2()
{
    wchar_t * data;
    wchar_t * dataBadBuffer = (wchar_t *)ALLOCA((10)*sizeof(wchar_t));
    wchar_t * dataGoodBuffer = (wchar_t *)ALLOCA((10+1)*sizeof(wchar_t));
    if(globalTrue)
    {
        data = dataGoodBuffer;
        data[0] = L'\0';
    }
    {
        wchar_t source[10+1] = SRC_STRING;
        wcsncpy(data, source, wcslen(source) + 1);
        printWLine(data);
    }
}

void CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_10_good()
{
    goodG2B1();
    goodG2B2();
}

#endif /* OMITGOOD */


 */

#ifdef INCLUDEMAIN

int main(int argc, char * argv[])
{
    /* seed randomness */
    srand( (unsigned)time(NULL) );
#ifndef OMITGOOD
    printLine("Calling good()...");
    CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_10_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
#ifndef OMITBAD
    printLine("Calling bad()...");
    CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_10_bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif
