from setuptools import find_packages, setup

package_name = 'simples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='robo2020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "action_server=simples.action_server:main",
            "action_client=simples.action_client:main",
            "service_server=simples.service_server:main",
            "service_client=simples.service_client:main",
            "service_client_timeout=simples.service_client_timeout:main"
        ],
    },
)
