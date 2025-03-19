def calculate_level(xp_current, levels):
    level = 0
    total_xp = 0
    
    for entry in levels:
        total_xp += entry["xpDelta"]
        if xp_current < total_xp:
            break
        level += 1
    
    return level

employee_levels = [
		{
			"xpDelta": 0,
			"statMain": 20
		},
		{
			"xpDelta": 20,
			"statMain": 28
		},
		{
			"xpDelta": 100,
			"statMain": 35
		},
		{
			"xpDelta": 350,
			"statMain": 40
		},
		{
			"xpDelta": 600,
			"statMain": 43
		},
		{
			"xpDelta": 688,
			"statMain": 46
		},
		{
			"xpDelta": 782,
			"statMain": 49
		},
		{
			"xpDelta": 882,
			"statMain": 52
		},
		{
			"xpDelta": 988,
			"statMain": 55
		},
		{
			"xpDelta": 1100,
			"statMain": 58
		},
		{
			"xpDelta": 1450,
			"statMain": 61
		},
		{
			"xpDelta": 2135,
			"statMain": 64
		},
		{
			"xpDelta": 2560,
			"statMain": 67
		},
		{
			"xpDelta": 2747,
			"statMain": 70
		},
		{
			"xpDelta": 2940,
			"statMain": 73
		},
		{
			"xpDelta": 3139,
			"statMain": 98
		},
		{
			"xpDelta": 4312,
			"statMain": 101
		},
		{
			"xpDelta": 4545,
			"statMain": 104
		},
		{
			"xpDelta": 4784,
			"statMain": 107
		},
		{
			"xpDelta": 5029,
			"statMain": 110
		},
		{
			"xpDelta": 5280,
			"statMain": 113
		},
		{
			"xpDelta": 5537,
			"statMain": 116
		},
		{
			"xpDelta": 5800,
			"statMain": 119
		},
		{
			"xpDelta": 6069,
			"statMain": 122
		},
		{
			"xpDelta": 6344,
			"statMain": 125
		},
		{
			"xpDelta": 6625,
			"statMain": 128
		},
		{
			"xpDelta": 6912,
			"statMain": 131
		},
		{
			"xpDelta": 7205,
			"statMain": 134
		},
		{
			"xpDelta": 7504,
			"statMain": 137
		},
		{
			"xpDelta": 7809,
			"statMain": 140
		},
		{
			"xpDelta": 8120,
			"statMain": 143
		},
		{
			"xpDelta": 8437,
			"statMain": 146
		},
		{
			"xpDelta": 8760,
			"statMain": 149
		},
		{
			"xpDelta": 10430,
			"statMain": 152
		},
		{
			"xpDelta": 12160,
			"statMain": 155
		},
		{
			"xpDelta": 15500,
			"statMain": 180
		},
		{
			"xpDelta": 19800,
			"statMain": 183
		},
		{
			"xpDelta": 20313,
			"statMain": 186
		},
		{
			"xpDelta": 20832,
			"statMain": 189
		},
		{
			"xpDelta": 21357,
			"statMain": 192
		},
		{
			"xpDelta": 21888,
			"statMain": 195
		},
		{
			"xpDelta": 22425,
			"statMain": 198
		},
		{
			"xpDelta": 22968,
			"statMain": 201
		},
		{
			"xpDelta": 23517,
			"statMain": 204
		},
		{
			"xpDelta": 24072,
			"statMain": 207
		},
		{
			"xpDelta": 24633,
			"statMain": 210
		},
		{
			"xpDelta": 25200,
			"statMain": 213
		},
		{
			"xpDelta": 25773,
			"statMain": 216
		},
		{
			"xpDelta": 26352,
			"statMain": 219
		},
		{
			"xpDelta": 26937,
			"statMain": 222
		},
		{
			"xpDelta": 27528,
			"statMain": 225
		},
		{
			"xpDelta": 28125,
			"statMain": 228
		},
		{
			"xpDelta": 28728,
			"statMain": 231
		},
		{
			"xpDelta": 29337,
			"statMain": 234
		},
		{
			"xpDelta": 29952,
			"statMain": 237
		},
		{
			"xpDelta": 30573,
			"statMain": 240
		},
		{
			"xpDelta": 31200,
			"statMain": 243
		},
		{
			"xpDelta": 31833,
			"statMain": 246
		},
		{
			"xpDelta": 32472,
			"statMain": 249
		},
		{
			"xpDelta": 33117,
			"statMain": 252
		},
		{
			"xpDelta": 33768,
			"statMain": 255
		},
		{
			"xpDelta": 34425,
			"statMain": 258
		},
		{
			"xpDelta": 35088,
			"statMain": 261
		},
		{
			"xpDelta": 35757,
			"statMain": 264
		},
		{
			"xpDelta": 36432,
			"statMain": 267
		},
		{
			"xpDelta": 37113,
			"statMain": 270
		},
		{
			"xpDelta": 37800,
			"statMain": 273
		},
		{
			"xpDelta": 40950,
			"statMain": 276
		},
		{
			"xpDelta": 44160,
			"statMain": 279
		},
		{
			"xpDelta": 47430,
			"statMain": 282
		},
		{
			"xpDelta": 50760,
			"statMain": 285
		},
		{
			"xpDelta": 51585,
			"statMain": 288
		},
		{
			"xpDelta": 52416,
			"statMain": 291
		},
		{
			"xpDelta": 53253,
			"statMain": 294
		},
		{
			"xpDelta": 54096,
			"statMain": 297
		},
		{
			"xpDelta": 54945,
			"statMain": 300
		},
		{
			"xpDelta": 55800,
			"statMain": 303
		},
		{
			"xpDelta": 56661,
			"statMain": 306
		},
		{
			"xpDelta": 57528,
			"statMain": 309
		},
		{
			"xpDelta": 58401,
			"statMain": 312
		},
		{
			"xpDelta": 59280,
			"statMain": 315
		},
		{
			"xpDelta": 62055,
			"statMain": 318
		},
		{
			"xpDelta": 66144,
			"statMain": 321
		},
		{
			"xpDelta": 70620,
			"statMain": 324
		},
		{
			"xpDelta": 74520,
			"statMain": 327
		},
		{
			"xpDelta": 78480,
			"statMain": 330
		},
		{
			"xpDelta": 82500,
			"statMain": 333
		},
		{
			"xpDelta": 86580,
			"statMain": 336
		},
		{
			"xpDelta": 90720,
			"statMain": 339
		},
		{
			"xpDelta": 94920,
			"statMain": 342
		},
		{
			"xpDelta": 99180,
			"statMain": 345
		},
		{
			"xpDelta": 103500,
			"statMain": 348
		},
		{
			"xpDelta": 104748,
			"statMain": 351
		},
		{
			"xpDelta": 106002,
			"statMain": 354
		},
		{
			"xpDelta": 107262,
			"statMain": 357
		},
		{
			"xpDelta": 108528,
			"statMain": 360
		},
		{
			"xpDelta": 109800,
			"statMain": 363
		},
		{
			"xpDelta": 111078,
			"statMain": 366
		},
		{
			"xpDelta": 112362,
			"statMain": 369
		},
		{
			"xpDelta": 113652,
			"statMain": 372
		},
		{
			"xpDelta": 114948,
			"statMain": 397
		},
		{
			"xpDelta": 123070,
			"statMain": 400
		},
		{
			"xpDelta": 124400,
			"statMain": 403
		},
		{
			"xpDelta": 125736,
			"statMain": 406
		},
		{
			"xpDelta": 127078,
			"statMain": 409
		},
		{
			"xpDelta": 128426,
			"statMain": 412
		},
		{
			"xpDelta": 129780,
			"statMain": 415
		},
		{
			"xpDelta": 131140,
			"statMain": 418
		},
		{
			"xpDelta": 132506,
			"statMain": 421
		},
		{
			"xpDelta": 133878,
			"statMain": 424
		},
		{
			"xpDelta": 135256,
			"statMain": 427
		},
		{
			"xpDelta": 136640,
			"statMain": 430
		},
		{
			"xpDelta": 138030,
			"statMain": 433
		},
		{
			"xpDelta": 139426,
			"statMain": 436
		},
		{
			"xpDelta": 140828,
			"statMain": 439
		},
		{
			"xpDelta": 142236,
			"statMain": 442
		},
		{
			"xpDelta": 143650,
			"statMain": 445
		},
		{
			"xpDelta": 145070,
			"statMain": 448
		},
		{
			"xpDelta": 146496,
			"statMain": 451
		},
		{
			"xpDelta": 147928,
			"statMain": 454
		},
		{
			"xpDelta": 149366,
			"statMain": 457
		},
		{
			"xpDelta": 150810,
			"statMain": 460
		},
		{
			"xpDelta": 152260,
			"statMain": 463
		},
		{
			"xpDelta": 153716,
			"statMain": 466
		},
		{
			"xpDelta": 155178,
			"statMain": 469
		},
		{
			"xpDelta": 156646,
			"statMain": 472
		},
		{
			"xpDelta": 158120,
			"statMain": 475
		},
		{
			"xpDelta": 159600,
			"statMain": 478
		},
		{
			"xpDelta": 161086,
			"statMain": 481
		},
		{
			"xpDelta": 162578,
			"statMain": 484
		},
		{
			"xpDelta": 164076,
			"statMain": 487
		},
		{
			"xpDelta": 165580,
			"statMain": 490
		},
		{
			"xpDelta": 167090,
			"statMain": 493
		},
		{
			"xpDelta": 168606,
			"statMain": 496
		},
		{
			"xpDelta": 170128,
			"statMain": 499
		},
		{
			"xpDelta": 171656,
			"statMain": 502
		},
		{
			"xpDelta": 173190,
			"statMain": 505
		},
		{
			"xpDelta": 174730,
			"statMain": 508
		},
		{
			"xpDelta": 176276,
			"statMain": 511
		},
		{
			"xpDelta": 177828,
			"statMain": 514
		},
		{
			"xpDelta": 179386,
			"statMain": 517
		},
		{
			"xpDelta": 180950,
			"statMain": 520
		},
		{
			"xpDelta": 189800,
			"statMain": 523
		},
		{
			"xpDelta": 193510,
			"statMain": 526
		},
		{
			"xpDelta": 197250,
			"statMain": 529
		},
		{
			"xpDelta": 201020,
			"statMain": 532
		},
		{
			"xpDelta": 204820,
			"statMain": 535
		},
		{
			"xpDelta": 208650,
			"statMain": 538
		},
		{
			"xpDelta": 212510,
			"statMain": 541
		},
		{
			"xpDelta": 216400,
			"statMain": 544
		},
		{
			"xpDelta": 220320,
			"statMain": 547
		},
		{
			"xpDelta": 224270,
			"statMain": 550
		},
		{
			"xpDelta": 228250,
			"statMain": 553
		},
		{
			"xpDelta": 232260,
			"statMain": 556
		},
		{
			"xpDelta": 236300,
			"statMain": 559
		},
		{
			"xpDelta": 240370,
			"statMain": 562
		},
		{
			"xpDelta": 244470,
			"statMain": 565
		},
		{
			"xpDelta": 248600,
			"statMain": 568
		},
		{
			"xpDelta": 252760,
			"statMain": 571
		},
		{
			"xpDelta": 256950,
			"statMain": 574
		},
		{
			"xpDelta": 261170,
			"statMain": 577
		},
		{
			"xpDelta": 265420,
			"statMain": 580
		},
		{
			"xpDelta": 269700,
			"statMain": 583
		},
		{
			"xpDelta": 274010,
			"statMain": 586
		},
		{
			"xpDelta": 278350,
			"statMain": 589
		},
		{
			"xpDelta": 282720,
			"statMain": 592
		},
		{
			"xpDelta": 287120,
			"statMain": 595
		},
		{
			"xpDelta": 291550,
			"statMain": 598
		},
		{
			"xpDelta": 296010,
			"statMain": 601
		},
		{
			"xpDelta": 300500,
			"statMain": 604
		},
		{
			"xpDelta": 305020,
			"statMain": 607
		},
		{
			"xpDelta": 309570,
			"statMain": 610
		},
		{
			"xpDelta": 314150,
			"statMain": 613
		},
		{
			"xpDelta": 318760,
			"statMain": 616
		},
		{
			"xpDelta": 323400,
			"statMain": 619
		},
		{
			"xpDelta": 328070,
			"statMain": 622
		},
		{
			"xpDelta": 332770,
			"statMain": 625
		},
		{
			"xpDelta": 337500,
			"statMain": 628
		},
		{
			"xpDelta": 342260,
			"statMain": 631
		},
		{
			"xpDelta": 347050,
			"statMain": 634
		},
		{
			"xpDelta": 351870,
			"statMain": 637
		},
		{
			"xpDelta": 356720,
			"statMain": 640
		},
		{
			"xpDelta": 361600,
			"statMain": 643
		},
		{
			"xpDelta": 366510,
			"statMain": 646
		},
		{
			"xpDelta": 371450,
			"statMain": 649
		},
		{
			"xpDelta": 376420,
			"statMain": 652
		},
		{
			"xpDelta": 381420,
			"statMain": 655
		},
		{
			"xpDelta": 386450,
			"statMain": 658
		},
		{
			"xpDelta": 391510,
			"statMain": 661
		},
		{
			"xpDelta": 396600,
			"statMain": 664
		},
		{
			"xpDelta": 401720,
			"statMain": 667
		},
		{
			"xpDelta": 406870,
			"statMain": 670
		},
		{
			"xpDelta": 412050,
			"statMain": 673
		},
		{
			"xpDelta": 417260,
			"statMain": 676
		},
		{
			"xpDelta": 422500,
			"statMain": 679
		},
		{
			"xpDelta": 427770,
			"statMain": 682
		},
		{
			"xpDelta": 433070,
			"statMain": 685
		},
		{
			"xpDelta": 438400,
			"statMain": 688
		},
		{
			"xpDelta": 443760,
			"statMain": 693
		},
		{
			"xpDelta": 443760,
			"statMain": 698
		}
	]

# xp_current = 892782
# level, stat_main = calculate_level(xp_current, employee_levels)
# print(f"Level: {level}, StatMain: {stat_main}")









employees = [
    {
        "id": 100002, "job": "GD", "baseStatMain": 1, "experience": 892782.643155978
    },
    {
        "id": 100003, "job": "DEV", "baseStatMain": 1, "experience": 904859.3243117569
    },
    {
        "id": 100005, "job": "DEV", "baseStatMain": 0, "experience": 869741.8852605763
    },
    {
        "id": 100000, "job": "GD", "baseStatMain": 10, "experience": 917708.1901773553
    },
    {
        "id": 100004, "job": "DEV", "baseStatMain": 5, "experience": 907782.5754655438
    },
    {
        "id": 100007, "job": "ART", "baseStatMain": 15, "experience": 734156.5561228138
    },
    {
        "id": 100008, "job": "ART", "baseStatMain": 0, "experience": 539063.4330918653
    },
    {
        "id": 100001, "job": "ART", "baseStatMain": 0, "experience": 388364.2189116324
    },
    {
        "id": 100006, "job": "ART", "baseStatMain": 2, "experience": 398597.3185482419
    },
    {
        "id": 100009, "job": "ART", "baseStatMain": 2, "experience": 126312.52300247493
    },
]


















# for employee in employees["employees"]:
    # level, stat_main = calculate_level(employee["experience"], employee_levels)
    # print(f"ID: {employee['id']}, Name: {employee['name']}, Level: {level}, StatMain: {stat_main}")
    
    
    
    
    
stat_main_sums = {"GD": 0, "DEV": 0, "ART": 0}

for emp in employees:
   
    level = calculate_level(emp["experience"], employee_levels)
    print (level)
    stat_main = employee_levels[level]["statMain"] + emp["baseStatMain"]
    stat_main_sums[emp["job"]] += stat_main
    

print(stat_main_sums)    
    