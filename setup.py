from setuptools import setup

package_name = 'py_camsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chris',
    maintainer_email='ivi3001@yahoo.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_camsub.publisher_member_function:main',
            'listener = py_camsub.subscriber_member_function:main',
            'camsub = py_camsub.camera_subscriber_member_function:main'
        ],
    },
)
