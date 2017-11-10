#include<bits/stdc++.h>
using namespace std;

float DAMPING_FACTOR = 0.85;
float EPSILON = 0.01;

void gaussSouthwell(vector<double> *x, double *P) {
	int N = (*x).size();
	float B = 1/((float)N);
	vector<double> xNew(N);
	vector<double> r;

	int i, j;
	for(i = 0; i < N; i++) {
		xNew[i] = 0;
		for(j = 0; j < N; j++) {
			xNew[i] += DAMPING_FACTOR*P[i*N+j];
		}
		xNew[i] += (1 - DAMPING_FACTOR)*B;
		r[i] = xNew[i] - (*x)[i];
	}

	while(true) {
		int maxRindex;
		double maxR = 0;
		for(i = 0; i < N; i++) {
			if (r[i] > maxR) {
				maxRindex = i;
				maxR = r[i];
			}
		}

		// checking for convergence
		if (maxR < EPSILON) {
			break;
		}

		// updating x
		(*x)[maxRindex] += maxR;

		// updating r
		r[maxRindex] = 0;
		for (i = 0; i < N; i++) {
			r[i] += DAMPING_FACTOR*maxR*(P[i*N+maxRindex]);
		}
	}
}

int main() {
	// cout<<"a";
	double* p=new double[4*4];
	p[0] = 0;
	p[1] = 0;
	p[2] = 0.5;
	p[3] = 0.5;

	p[4]= 0.33;
	p[5] = 0;
	p[6] = 0;
	p[7] = 0;

	p[8] = 0.33;
	p[9] = 0;
	p[10] = 0;
	p[11] = 0.5;

	p[12] = 0.33;
	p[13] = 1;
	p[14] = 0.5;
	p[15] = 0;

	vector<double> x(4);
	x[0] = 1;
	x[1] = 1;
	x[2] = 1;
	x[3] = 1;
	
	cout<<"a";
	gaussSouthwell(&x, p);

	// cout<<x;
}
