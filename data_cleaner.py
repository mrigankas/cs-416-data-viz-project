import csv
# import pandas as pd


def main():
    with open('us_statewise_covid_data.csv', 'r') as fi:
        reader = csv.DictReader(fi)
        sorted_lines = sorted(reader, key=lambda row:(row['date'], row['state']), reverse=False)

        with open('us_statewise_covid_data_cleaned.csv', 'w') as fo:
            fieldnames = ['state', 'date', 'total_adult_patients_hospitalized_confirmed_and_suspected_covid',
                          'total_adult_patients_hospitalized_confirmed_and_suspected_covid_coverage',
                          'total_adult_patients_hospitalized_confirmed_covid',
                          'total_adult_patients_hospitalized_confirmed_covid_coverage',
                          'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid',
                          'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_coverage',
                          'total_pediatric_patients_hospitalized_confirmed_covid',
                          'total_pediatric_patients_hospitalized_confirmed_covid_coverage', 'deaths_covid']
            writer = csv.DictWriter(fo, fieldnames=fieldnames)
            writer.writeheader()

            # for row in reader:
            for row in sorted_lines:
                if ((row['total_adult_patients_hospitalized_confirmed_and_suspected_covid'] and
                        int(row['total_adult_patients_hospitalized_confirmed_and_suspected_covid']) > 0) and
                        (row['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid'] and
                         int(row['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid']) > 0) and
                        (row['deaths_covid'] and int(row['deaths_covid']) > 0) and
                        (row['date'] > "2020/06/30")):
                    # print(row)
                    # writer.writerow(row)
                    writer.writerow({'state':row['state'], 'date':row['date'],
                                     'total_adult_patients_hospitalized_confirmed_and_suspected_covid':
                                         row['total_adult_patients_hospitalized_confirmed_and_suspected_covid'],
                                     'total_adult_patients_hospitalized_confirmed_and_suspected_covid_coverage':
                                         row['total_adult_patients_hospitalized_confirmed_and_suspected_covid_coverage'],
                                     'total_adult_patients_hospitalized_confirmed_covid':
                                         row['total_adult_patients_hospitalized_confirmed_covid'],
                                     'total_adult_patients_hospitalized_confirmed_covid_coverage':
                                         row['total_adult_patients_hospitalized_confirmed_covid_coverage'],
                                     'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid':
                                         row['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid'],
                                     'total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_coverage':
                                         row['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_coverage'],
                                     'total_pediatric_patients_hospitalized_confirmed_covid':
                                         row['total_pediatric_patients_hospitalized_confirmed_covid'],
                                     'total_pediatric_patients_hospitalized_confirmed_covid_coverage':
                                         row['total_pediatric_patients_hospitalized_confirmed_covid_coverage'],
                                     'deaths_covid':row['deaths_covid']})

    # data_frame = pd.read_csv('us_statewise_covid_data_cleaned.csv')
    # data_frame.sort_values(['date', 'state'], axis=0, ascending=True, inplace=True, na_position='first')


if __name__ == '__main__':
    main()