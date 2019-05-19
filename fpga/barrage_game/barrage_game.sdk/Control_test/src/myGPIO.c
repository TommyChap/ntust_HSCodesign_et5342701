

/***************************** Include Files *******************************/
#include "myGPIO.h"
#include "xparameters.h"

/************************** Function Definitions ***************************/

u32 mygpio_read(u32 select){
	//implement your driver
	return MYGPIO_mReadReg(XPAR_CONTROLANDDISPLAYIP_0_S00_AXI_BASEADDR, select * 4);
}
void mygpio_write(u32 data, u32 select){
	//implement your driver
	MYGPIO_mWriteReg(XPAR_CONTROLANDDISPLAYIP_0_S00_AXI_BASEADDR, select * 4, data);
}
