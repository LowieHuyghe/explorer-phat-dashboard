
if __name__ == '__main__':
    import os.path
    from explorerphatdashboard.dashboard import Dashboard

    base_path = os.path.dirname(os.path.realpath(__file__))
    dashboard = Dashboard(base_path)
    dashboard.run()
