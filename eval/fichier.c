#include "../include/layers.h"


void conv1 (float* weights, float* bias, float input[28][28], float output[28][28][6]) {
	//Temporary input for padded input
	float input_temp[32][32];
	//Add padding at the input
	padding(input, input_temp);
	//Filter position
	for (int r = 0; r < 28; r++) {
		for (int c = 0; c < 28; c++) {
			//Select the filter
			for (int f = 0; f < 6; f++) {
				//Accumulator to store weights and input multiplication
				float acc = 0;
				//Multiply the input patch and weights of filter f
				for (int fr = 0; fr < 5; fr++) {
					for (int fc = 0; fc < 5; fc++) {
						acc += weights[fr*30 + fc*6 + f] * input_temp[r + fr][c + fc];
					}
				}
				//Acitvation function
				acc += bias[f];
				output[r][c][f] = relu_activation(acc);
			}
		}
	}
}

void maxPooling1(float input[28][28][6], float output[14][14][6]) {
	//Temporary variables
	float max;
	float temp;
	//Iterates over the input tensor
	for (int fm = 0; fm < 6; fm++) {
		for (int r = 0; r < 28; r += 2) {
			for (int c = 0; c < 28; c += 2) {
				max = 0;
				//Iterates over the filter to get the maximum value
				for (int fr = 0; fr < 2; fr++) {
					for (int fc = 0; fc < 2; fc++) {
						temp = input[r + fr][c + fc][fm];
						if(temp > max)
							max = temp;
					}
				}
				//Save the maximum value on the output tensor
				output[r/2][c/2][fm] = max;
			}
		}
	}
}

void conv2 (float* weights, float* bias, float input[14][14][6], float output[10][10][16]) {
	//Iterate over the input
for (int r = 0; r < 10; r++) {
		for (int c = 0; c < 10; c++) {
			//Select the filter
			for (int f = 0; f < 16; f++) {
				//Accumulator to store weights and input multiplication
				float acc = 0;
				//Multiply the input patch and weights of filter f
				for (int fm = 0; fm < 6; fm++) {
					for (int fr = 0; fr < 5; fr++) {
						for (int fc = 0; fc < 5; fc++) {
							acc += weights[fr*480 + fc*96 + fm*16 + f] * input[r + fr][c + fc][fm];
						}
					}
				}
				//Store the calculated value in the output
				acc += bias[f];
				output[r][c][f] = relu_activation(acc);
			}
		}
	}
}

void maxPooling2(float input[10][10][16], float output[5][5][16]) {
	//Temporary variables
	float max;
	float temp;
	//Iterates over the input tensor
	for (int fm = 0; fm < 16; fm++)	{
		for (int r = 0; r < 10; r += 2) {
			for (int c = 0; c < 10; c += 2) {
				max = 0;
				//Iterates over the filter to get the maximum value
				for (int kr = 0; kr < 2; kr++) {
					for (int kc = 0; kc < 2; kc++) {
						temp = input[r + kr][c + kc][fm];
						if(temp > max)
							max = temp;
					}
				}
				//Save the maximum value on the output tensor
				output[r/2][c/2][fm] = max;
			}
		}
	}
}

void conv3(float* weights, float* bias, float input[5][5][16], float output[120]) {
	//Iterate over the input
	for (int f = 0; f < 120; f++) {
		//Accumulator of matrix multiplication
		float acc = 0;
		//Multiply all filter weights with all patch values
		for (int fm = 0; fm < 16; fm++) {
			for (int kr = 0; kr < 5; kr++) {
				for (int kc = 0; kc < 5; kc++) {
					acc += weights[kr*9600 + kc*1920 + fm*120 + f] * input[kr][kc][fm];
				}
			}
		}
		//Add bias and write output
		acc += bias[f];
		output[f] = relu_activation(acc);		
	}
}

void dense1(float* weights, float* bias, float input[120], float output[84]) {
	//Temporary variables
	float acc;
	//Dot product between the input array and weights matrix
	for (int r = 0; r < 84; r++) {
		acc = 0;
		for (int c = 0; c < 120; c++) {
			acc += input[c] * weights[c*84 + r];
		}
		//Add bias and write output
		acc += bias[r];
		output[r] = relu_activation(acc);
	}
}

void dense2(float* weights, float* bias,
			float input[84], float output[10]) {
	//Temporary variables
	float acc;
	//Dot product between the input array and weights matrix
	for (int r = 0; r < 10; r++) {
		acc = 0;
		for (int c = 0; c < 84; c++) {
			acc += input[c] * weights[c*10 + r];
		}
		//Add bias and write output
		output[r] = acc + bias[r];
	}
}
