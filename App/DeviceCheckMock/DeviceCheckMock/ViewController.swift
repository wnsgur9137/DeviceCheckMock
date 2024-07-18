//
//  ViewController.swift
//  DeviceCheckMock
//
//  Created by JunHyeok Lee on 7/18/24.
//

import UIKit
import DeviceCheck

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        loadDeviceToken()
    }

    private func loadDeviceToken() {
        let curDevice = DCDevice.current
        guard curDevice.isSupported else { return } // Simulator의 경우 사용할 수 없음
        Task {
            do {
                let token = try await curDevice.generateToken()
                let tokenString = token.base64EncodedString()
                print("token: \(tokenString)")
                // Device Token 서버로 전송
            } catch {
                print("error: \(error.localizedDescription)")
            }
        }
    }
    
    private func loadDeviceToken2() {
        let curDevice = DCDevice.current
        guard curDevice.isSupported else { return }
        curDevice.generateToken() { (token, error) in
            if let error = error {
                print("error: \(error.localizedDescription)")
                return
            }
            guard let token = token else { return }
            let tokenString = token.base64EncodedString()
            print("token: \(tokenString)")
        }
    }
}

