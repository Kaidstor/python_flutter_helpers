import os
import sys

def mkdir(dir):
    if not (os.path.exists(dir)):
        os.mkdir(dir)

command = sys.argv[1]
feature_name = sys.argv[2]

def mkdir(dir):
    if not (os.path.exists(dir)):
        os.mkdir(dir)

feature_camel_case = ''.join([word.title() for word in feature_name.split('_')])

screen_text = f"""import 'package:flutter/material.dart';

class {feature_camel_case}Screen extends StatelessWidget {{
  const {feature_camel_case}Screen({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return const Placeholder();
  }}
}}
"""

if (command == 'new'):
    
    common_dir = './lib/features/'

    feature_dir = common_dir + sys.argv[2]

    view_dir = f'{common_dir + feature_name}/view'
    bloc_dir = f'{common_dir + feature_name}/bloc'
    widget_dir = f'{common_dir + feature_name}/widgets'

    mkdir(feature_dir);
    mkdir(view_dir);
    mkdir(bloc_dir);
    mkdir(widget_dir);

    with open(f'{feature_dir}/view.dart', 'w') as f:
        f.write(f'export "./view/view.dart";')

    # view folder 
    with open(f'{view_dir}/view.dart', 'w') as f:
        f.write(f'export "{feature_name}_screen.dart";')
        
    with open(f'{view_dir}/{feature_name}_screen.dart', 'w') as f:
        f.write(screen_text)


    # bloc folder  
    with open(f'{bloc_dir}/{feature_name}_bloc.dart', 'w') as f:
        f.write('')

    with open(f'{bloc_dir}/{feature_name}_state.dart', 'w') as f:
        f.write('')

    with open(f'{bloc_dir}/{feature_name}_event.dart', 'w') as f:
        f.write('')

else: 
    print('Unknown command')
    
    