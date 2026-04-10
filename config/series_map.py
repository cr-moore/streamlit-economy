series_dict = {
    # Utilities & Fuel
    'APU000072511':  {'name': 'fuel oil #2',                              'unit': 'per gal'},
    'APU000072610':  {'name': 'electricity',                              'unit': 'per KWH'},
    'APU000072620':  {'name': 'utility gas (piped)',                      'unit': 'per therm'},
    'APU000074714':  {'name': 'gasoline (unleaded regular)',              'unit': 'per gal'},
    'APU000074715':  {'name': 'gasoline (unleaded midgrade)',             'unit': 'per gal'},
    'APU000074716':  {'name': 'gasoline (unleaded premium)',              'unit': 'per gal'},
    'APU000074717':  {'name': 'automotive diesel fuel',                   'unit': 'per gal'},
    'APU00007471A':  {'name': 'gasoline (all types)',                     'unit': 'per gal'},

    # Grains & Bread
    'APU0000701111': {'name': 'flour (white, all purpose)',               'unit': 'per lb'},
    'APU0000701312': {'name': 'rice (white, long grain, uncooked)',       'unit': 'per lb'},
    'APU0000701322': {'name': 'spaghetti and macaroni',                   'unit': 'per lb'},
    'APU0000702111': {'name': 'bread (white)',                            'unit': 'per lb'},
    'APU0000702112': {'name': 'bread (French)',                           'unit': 'per lb'},
    'APU0000702212': {'name': 'bread (whole wheat)',                      'unit': 'per lb'},
    'APU0000702421': {'name': 'cookies (chocolate chip)',                 'unit': 'per lb'},

    # Beef
    'APU0000703111': {'name': 'ground chuck (100% beef)',                 'unit': 'per lb'},
    'APU0000703112': {'name': 'ground beef (100% beef)',                  'unit': 'per lb'},
    'APU0000703113': {'name': 'ground beef (lean and extra lean)',        'unit': 'per lb'},
    'APU0000703212': {'name': 'chuck roast (excl. USDA Prime/Choice)',   'unit': 'per lb'},
    'APU0000703213': {'name': 'chuck roast (USDA Choice, boneless)',     'unit': 'per lb'},
    'APU0000703311': {'name': 'round roast (USDA Choice, boneless)',     'unit': 'per lb'},
    'APU0000703431': {'name': 'short ribs (bone-in)',                     'unit': 'per lb'},
    'APU0000703432': {'name': 'beef for stew (boneless)',                 'unit': 'per lb'},
    'APU0000703511': {'name': 'steak, round (USDA Choice, boneless)',    'unit': 'per lb'},
    'APU0000703512': {'name': 'steak, round (excl. USDA Prime/Choice)',  'unit': 'per lb'},
    'APU0000703613': {'name': 'steak, sirloin (USDA Choice, boneless)',  'unit': 'per lb'},
    'APU0000FC1101': {'name': 'all uncooked ground beef',                 'unit': 'per lb'},
    'APU0000FC2101': {'name': 'all uncooked beef roasts',                 'unit': 'per lb'},
    'APU0000FC3101': {'name': 'all uncooked beef steaks',                 'unit': 'per lb'},
    'APU0000FC4101': {'name': 'all uncooked other beef (excl. veal)',    'unit': 'per lb'},

    # Pork
    'APU0000704111': {'name': 'bacon (sliced)',                           'unit': 'per lb'},
    'APU0000704211': {'name': 'pork chops (center cut, bone-in)',        'unit': 'per lb'},
    'APU0000704212': {'name': 'pork chops (boneless)',                    'unit': 'per lb'},
    'APU0000704311': {'name': 'ham (rump/shank half, bone-in, smoked)', 'unit': 'per lb'},
    'APU0000704312': {'name': 'ham (boneless, excl. canned)',            'unit': 'per lb'},
    'APU0000FD2101': {'name': 'all ham (excl. canned/luncheon slices)', 'unit': 'per lb'},
    'APU0000FD3101': {'name': 'all pork chops',                          'unit': 'per lb'},
    'APU0000FD4101': {'name': 'all other pork',                          'unit': 'per lb'},

    # Poultry & Other Meats
    'APU0000705111': {'name': 'frankfurters (all meat or all beef)',     'unit': 'per lb'},
    'APU0000705121': {'name': 'bologna (all beef or mixed)',              'unit': 'per lb'},
    'APU0000706111': {'name': 'chicken (fresh, whole)',                   'unit': 'per lb'},
    'APU0000706212': {'name': 'chicken legs (bone-in)',                   'unit': 'per lb'},
    'APU0000706311': {'name': 'turkey (frozen, whole)',                   'unit': 'per lb'},
    'APU0000707111': {'name': 'tuna (light, chunk)',                      'unit': 'per lb'},
    'APU0000FF1101': {'name': 'chicken breast (boneless)',                'unit': 'per lb'},

    # Dairy & Eggs
    'APU0000708111': {'name': 'eggs (Grade A, large)',                   'unit': 'per dozen'},
    'APU0000708112': {'name': 'eggs (Grade AA, large)',                  'unit': 'per dozen'},
    'APU0000709112': {'name': 'milk (whole, fortified)',                  'unit': 'per gal'},
    'APU0000710211': {'name': 'cheese (American processed)',              'unit': 'per lb'},
    'APU0000710212': {'name': 'cheese (cheddar, natural)',               'unit': 'per lb'},
    'APU0000710411': {'name': 'ice cream (bulk, regular)',               'unit': 'per 1/2 gal'},
    'APU0000FJ1101': {'name': 'milk (low-fat/skim)',                     'unit': 'per gal'},
    'APU0000FJ4101': {'name': 'yogurt',                                   'unit': 'per 8 oz'},

    # Fruits & Vegetables
    'APU0000711211': {'name': 'bananas',                                  'unit': 'per lb'},
    'APU0000711311': {'name': 'oranges (Navel)',                         'unit': 'per lb'},
    'APU0000711411': {'name': 'grapefruit',                               'unit': 'per lb'},
    'APU0000711412': {'name': 'lemons',                                   'unit': 'per lb'},
    'APU0000711413': {'name': 'pears (Anjou)',                           'unit': 'per lb'},
    'APU0000711414': {'name': 'peaches',                                  'unit': 'per lb'},
    'APU0000711415': {'name': 'strawberries',                             'unit': 'per 12 oz'},
    'APU0000711417': {'name': 'grapes (Thompson Seedless)',              'unit': 'per lb'},
    'APU0000711418': {'name': 'cherries',                                 'unit': 'per lb'},
    'APU0000712112': {'name': 'potatoes (white)',                        'unit': 'per lb'},
    'APU0000712211': {'name': 'lettuce (iceberg)',                       'unit': 'per lb'},
    'APU0000712311': {'name': 'tomatoes (field grown)',                  'unit': 'per lb'},
    'APU0000712406': {'name': 'peppers (sweet)',                         'unit': 'per lb'},
    'APU0000712412': {'name': 'broccoli',                                 'unit': 'per lb'},
    'APU0000FL2101': {'name': 'lettuce (romaine)',                       'unit': 'per lb'},

    # Packaged & Other Foods
    'APU0000713111': {'name': 'orange juice (frozen concentrate)',       'unit': 'per 16 oz'},
    'APU0000714221': {'name': 'corn (canned)',                           'unit': 'per lb'},
    'APU0000714233': {'name': 'beans (dried, any type)',                 'unit': 'per lb'},
    'APU0000715211': {'name': 'sugar (white, all sizes)',               'unit': 'per lb'},
    'APU0000715212': {'name': 'sugar (white, 33-80 oz pkg)',            'unit': 'per lb'},
    'APU0000716116': {'name': 'margarine (soft, tubs)',                  'unit': 'per lb'},
    'APU0000717311': {'name': 'coffee (ground roast)',                   'unit': 'per lb'},
    'APU0000718311': {'name': 'potato chips',                            'unit': 'per lb'},
    'APU0000FS1101': {'name': 'butter (sticks)',                         'unit': 'per lb'},

    # Beverages & Alcohol
    'APU0000720111': {'name': 'beer (all types)',                        'unit': 'per 16 oz'},
    'APU0000720222': {'name': 'vodka (all types)',                       'unit': 'per liter'},
    'APU0000720311': {'name': 'wine (red and white table)',              'unit': 'per liter'},
    'APU0000FN1101': {'name': 'soft drinks',                             'unit': 'per 2 liter'},
    'APU0000FN1102': {'name': 'soft drinks (12-pack)',                   'unit': 'per 12 oz can'}
}