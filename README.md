# FPAX
FPAX is a framework for exploring approximate configurations, which utilizes prior knowledge to guide DSE, thus avoiding a large amount of redundant calculations and achieving high-quality approximate configurations in a short amount of time.
Before using FPAX, we need to guide the following requirements：


(1) The application needs to generate CDFG files through GAUT[1].

(2) Combine the CDFG file of the application to form the corresponding calculation function file (for example, applications/laplacecomputing. py).

(3) DSE.py is the main.py. We can run DSE.py to get the results.

(4) model.pt is a trained NN model.

Using FPAX:

(1) The applied CDFG file needs to be parsed through Fileparsing (open Fileparsing.py and replace the file name).

![image](https://github.com/douyuqin/FPAX/assets/76696712/74b5af4a-fc51-4d30-81d3-dac4ef3182f8)

(2) Open computing.py, lines 32 and 36 need to be replaced according to the calculation function file.

![image](https://github.com/douyuqin/FPAX/assets/76696712/5ca2752f-8545-435c-81f8-b15ce048d8ba)


(3) Open DSE.py, select the error constraint.

![image](https://github.com/douyuqin/FPAX/assets/76696712/e7b6833d-a3f9-4739-bcad-9a4e569dcb51)

(4) Run ENAP.py

[1] E. Martin, O. Sentieys, H. Dubois, and J. L. Philippe, “GAUT: Anarchitectural synthesis tool for dedicated signal processors,” in European Design Automation Conference, 1993
