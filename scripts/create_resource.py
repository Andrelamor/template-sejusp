import os
import sys
from frictionless import Package

def create_resource():
  local_package = Package('datapackage.json')
  datapackage_resouces_names = [i["name"] for i in local_package.resources]
  for name in datapackage_resouces_names:
    sys.exec(dpckan resource create name)

if __name__ == '__main__':
  create_resource()