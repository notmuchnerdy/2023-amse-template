# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes the correlation between total bike counts in Konstanz in an hour and the count of bike-involved traffic accidents. Besides, how the weather parameters such as temperature, and precipitation affect bike counts on the traffic and bike-involved accidents will be analyzed. Moreover, an ML prediction model on possible bike counts will be obtained based on the temperature and weather parameters. 

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Thanks to this analysis, traffic alerts can be designed for notifying drivers about high bike count expectancy on the road. According to the location information, extra safety measures can be suggested for the places which have high traffic accident potential under the time and weather circumstances.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ZAEHLSTELLE_HEROSE_2020_STUENDLICH_WETTER
* Metadata URL: https://mobilithek.info/offers/-7161835583190029268
* Data URL: https://offenedaten-konstanz.de/dataset/fahrrad-dauerz-hlstellen/resource/c7da262a-7f4e-41a4-9a57-1d41222d77a4
* Data Type: CSV

Short description.

### Datasource2: ZAEHLSTELLE_HEROSE_2020_STUENDLICH_WETTER
* Metadata URL: https://offenedaten-konstanz.de/dataset/stra-enverkehrsunf-lle/resource/ea89132c-c4f2-40e0-b276-37d2d955e7fa
* Data URL: https://offenedaten-konstanz.de/dataset/stra-enverkehrsunf-lle/resource/fd1ac960-6b74-448e-bb82-23b35467a5f4
* Data Type: CSV

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
1. ETL Operations on the datasets [#1]
2. Merging two datasets [#2]
3. Correlation analysis on bike counts and bike-involved traffic accidents [#3]
4. Correlation analysis on weather, time, bike count and accidents [#4]
5. ML prediction model design which estimates possible bike count on traffic [#5]
6. Discussion on the results [#6]

8. Example Issue [#1][i1]
9. ...

[i1]: https://github.com/jvalue/2023-amse-template/issues/19
[i2]: https://github.com/jvalue/2023-amse-template/issues/20
[i3]: https://github.com/jvalue/2023-amse-template/issues/21
[i4]: https://github.com/jvalue/2023-amse-template/issues/22
[i5]: https://github.com/jvalue/2023-amse-template/issues/23
[i6]: https://github.com/jvalue/2023-amse-template/issues/24
