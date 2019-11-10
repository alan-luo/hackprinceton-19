var source_data = {
"buzzfeed": 			{'Bias': -68, 'Impact': 3.00, 'Locality': 0.10, 'Sensationalism': 0.96, 'Writing Quality': 0.24, 'Credibility': 0.28, 'Updatedness': 0.70},
"the-huffington-post": 	{'Bias': -61, 'Impact': 5.00, 'Locality': 0.40, 'Sensationalism': 0.98, 'Writing Quality': 0.48, 'Credibility': 0.15, 'Updatedness': 0.92},
"msnbc": 				{'Bias': -52, 'Impact': 4.60, 'Locality': 0.30, 'Sensationalism': 0.87, 'Writing Quality': 0.76, 'Credibility': 0.28, 'Updatedness': 0.94},
"the-new-yorker": 		{'Bias': -48, 'Impact': 4.20, 'Locality': 0.48, 'Sensationalism': 0.56, 'Writing Quality': 0.70, 'Credibility': 0.90, 'Updatedness': 0.86},
"the-guardian": 		{'Bias': -34, 'Impact': 4.50, 'Locality': 0.18, 'Sensationalism': 0.72, 'Writing Quality': 0.68, 'Credibility': 0.98, 'Updatedness': 0.92},
"the-washington-post": 	{'Bias': -25, 'Impact': 5.70, 'Locality': 0.34, 'Sensationalism': 0.43, 'Writing Quality': 0.62, 'Credibility': 0.94, 'Updatedness': 0.78},
"the-new-york-times": 	{'Bias': -25, 'Impact': 9.70, 'Locality': 0.26, 'Sensationalism': 0.68, 'Writing Quality': 0.90, 'Credibility': 1.00, 'Updatedness': 1.00},
"politico": 			{'Bias': -17, 'Impact': 3.60, 'Locality': 0.32, 'Sensationalism': 0.24, 'Writing Quality': 0.76, 'Credibility': 0.92, 'Updatedness': 0.64},
"bbc-news": 			{'Bias': -10, 'Impact': 9.80, 'Locality': 0.52, 'Sensationalism': 0.10, 'Writing Quality': 0.92, 'Credibility': 0.98, 'Updatedness': 0.86},
"cnn": 					{'Bias': -14, 'Impact': 9.50, 'Locality': 0.28, 'Sensationalism': 0.59, 'Writing Quality': 0.84, 'Credibility': 1.00, 'Updatedness': 0.94},
"nbc-news": 			{'Bias': -6, 'Impact': 8.70, 'Locality': 0.26, 'Sensationalism': 0.57, 'Writing Quality': 0.78, 'Credibility': 0.94, 'Updatedness': 0.98},
"usa-toda": 			{'Bias': 0, 'Impact': 5.40, 'Locality': 0.22, 'Sensationalism': 0.78, 'Writing Quality': 0.50, 'Credibility': 0.98, 'Updatedness': 0.76},
"abc-news": 			{'Bias': -1, 'Impact': 8.20, 'Locality': 0.10, 'Sensationalism': 0.35, 'Writing Quality': 0.86, 'Credibility': 0.67, 'Updatedness': 0.94},
"cbs-new": 				{'Bias': 4, 'Impact': 6.50, 'Locality': 0.16, 'Sensationalism': 0.28, 'Writing Quality': 0.94, 'Credibility': 0.94, 'Updatedness': 0.96},
"the-wall-street-journal": {'Bias': 	3, 'Impact': 5.90, 'Locality': 0.26, 'Sensationalism': 0.03, 'Writing Quality': 0.94, 'Credibility': 1.00, 'Updatedness': 0.76},
"bloomber": 			{'Bias': 0, 'Impact': 6.80, 'Locality': 0.34, 'Sensationalism': 0.52, 'Writing Quality': 0.90, 'Credibility': 0.98, 'Updatedness': 0.72},
"the-washington-time": 	{'Bias': 	17, 'Impact': 4.10, 'Locality': 0.10, 'Sensationalism': 0.63, 'Writing Quality': 0.76, 'Credibility': 0.82, 'Updatedness': 0.74},
"fox-new": 				{'Bias': 39, 'Impact': 9.50, 'Locality': 0.36, 'Sensationalism': 0.89, 'Writing Quality': 0.64, 'Credibility': 0.60, 'Updatedness': 0.99},
"breitbart-new": 		{'Bias': 84, 'Impact': 2.00, 'Locality': 0.34, 'Sensationalism': 0.99, 'Writing Quality': 0.28, 'Credibility': 0.04, 'Updatedness': 0.70},
};