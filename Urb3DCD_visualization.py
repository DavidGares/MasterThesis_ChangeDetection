"""
USAGE: python Urb3DCD_visualization.py -pc path/to/point/cloud/to/visualize.ply
Tool to visualize binary .ply point clouds from the Urb3DCD-v2 dataset:
https://ieee-dataport.org/open-access/urb3dcd-urban-point-clouds-simulated-dataset-3d-change-detection
"""
import argparse
import os
import plyfile
import numpy as np
import open3d as o3d


def visualize_point_cloud(ply_file_path):
    # Extract the name of the point cloud from the path
    pc_name = os.path.basename(ply_file_path).split('.')[0]

    # Read the PLY file
    plydata = plyfile.PlyData.read(ply_file_path)

    # Extract vertex data
    x = plydata['params']['x']
    y = plydata['params']['y']
    z = plydata['params']['z']

    # Create an Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.column_stack((x, y, z)))

    # Customize visualization parameters
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=pc_name)  # Set window title to the name of the point cloud
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0])  # Set background color to black
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Visualize a point cloud from a PLY file.")
    parser.add_argument("--pointcloud", "-pc",
                        default='/home/dge95/Desktop/Urb3DCD-V2/IEEE_Dataset_V2_Lid05_MS/1-Lidar05/Train/LyonN14/pointCloud0.ply',
                        help="Path to the PLY file")

    # Parse command-line arguments
    args = parser.parse_args()

    # Check if the point cloud path is provided
    if args.pointcloud:
        # Visualize the point cloud
        visualize_point_cloud(args.pointcloud)
    else:
        print("Error: Please provide the path to the point cloud using --pointcloud or -pc option.")


if __name__ == "__main__":
    main()
