OPENQASM 2.0;
include "qelib1.inc";
gate c7_1_mod_15 q0,q1,q2,q3,q4 { ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; }
gate c7_2_mod_15 q0,q1,q2,q3,q4 { ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; }
gate c7_8_mod_15 q0,q1,q2,q3,q4 { ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; }
gate c7_128_mod_15 q0,q1,q2,q3,q4 { ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; ccx q0,q3,q4; ccx q0,q4,q3; ccx q0,q3,q4; ccx q0,q2,q3; ccx q0,q3,q2; ccx q0,q2,q3; ccx q0,q1,q2; ccx q0,q2,q1; ccx q0,q1,q2; cx q0,q1; }
gate gate_IQFT q0,q1,q2,q3 { h q0; cp(-pi/2) q1,q0; h q1; cp(-pi/4) q2,q0; cp(-pi/2) q2,q1; h q2; cp(-pi/8) q3,q0; cp(-pi/4) q3,q1; cp(-pi/2) q3,q2; h q3; }
gate gate_IQFT_2398713115552 q0,q1,q2,q3 { gate_IQFT q0,q1,q2,q3; }
qreg q[8];
creg c[4];
h q[0];
h q[1];
h q[2];
h q[3];
c7_1_mod_15 q[0],q[4],q[5],q[6],q[7];
c7_2_mod_15 q[1],q[4],q[5],q[6],q[7];
c7_8_mod_15 q[2],q[4],q[5],q[6],q[7];
c7_128_mod_15 q[3],q[4],q[5],q[6],q[7];
gate_IQFT_2398713115552 q[0],q[1],q[2],q[3];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
