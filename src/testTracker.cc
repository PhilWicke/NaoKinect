#include "NiTE.h"
#include "../Common/NiteSampleUtilities.h"

using namespace nite;

niteRC = NiTE::initialize();
if (niteRC != STATUS_OK)
{
    printf("NiTE initialization failed\n");
    return 1;

}
