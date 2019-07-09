def non_hotel():
    """
    Eat at Hotel 19, 24, 28  June 2019
    :return:
    """
    # 17 June 2019
    taxi_go_thb = 350
    toll_way_thb = 120
    sim_card_rupiah, sim_card_thb = 350000, 786.80

    # 18 June 2019
    tea_time_lunch_rupiah, tea_time_lunch_thb = 61000, 137.12

    # 20 June 2019
    lotte_ottoya_rupiah, lotte_ottoya_thb = 176100, 397.41

    # 22 June 2019
    ikea_lunch_rupiah, ikea_lunch_thb = 125000, 279.86

    # 23 June 2019
    burgreen_lunch_rupiah, burgreen_lunch_thb = 180923, 405.05

    # 25 June 2019
    lunch_tempo_scan_rupiah, lunch_tempo_scan_thb = 48400, 108.23
    redsun_dinner_rupiah, redsun_dinner_thb = 77385, 173.04
    blacklisted_dinner_rupiah, blacklisted_dinner_thb = 123013, 275.06

    # 26 June 2019
    lunch_tempo_scan_2_rupiah, lunch_tempo_scan_2_thb = 67000, 149.94

    # 27 June 2019
    lunch_tempo_scan_3_rupiah, lunch_tempo_scan_3_thb = 58000, 129.42

    # 29 June 2019
    lunch_airport_rupiah, lunch_airport_thb = 118000, 264.31
    taxi_to_home_thb = 290  # THB

    return taxi_go_thb + toll_way_thb + sim_card_thb + tea_time_lunch_thb + lotte_ottoya_thb + ikea_lunch_thb + burgreen_lunch_thb \
           + lunch_tempo_scan_thb + redsun_dinner_thb + blacklisted_dinner_thb + lunch_tempo_scan_2_thb + lunch_tempo_scan_3_thb \
           + lunch_airport_thb + taxi_to_home_thb


def main():
    hotel = 69283.53 # THB
    expense = non_hotel()
    print(f"{expense} THB")  # 3636.24
    print(f"total: {hotel + expense}")  # 73149.77


if __name__ == '__main__':
    main()
