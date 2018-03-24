//
//  InputViewController.swift
//  pitScouting
//
//  Created by Vrishab Madduri on 3/20/18.
//  Copyright © 2018 Vrishab Madduri. All rights reserved.
//

import Foundation
import UIKit
import QRCode 


class InputViewController: UIViewController {
    @IBOutlet weak var teamLabel: UILabel!
    
    @IBAction func doneButton(_ sender: Any) {
       print("called")
        
        let alert = UIAlertController(title: "Exiting", message: "Are you sure you are done?", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .`default`, handler: { _ in
            self.performSegue(withIdentifier: "doneSegue", sender: sender)
        }))
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("Cancel", comment: "Default action"), style: .`default`, handler: { _ in
        }))
        
        self.present(alert, animated: true, completion: nil)
    }
    
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        teamLabel.text = "Team #: \(State.global.team)"
        let text = """
\(State.global.team)|\(State.global.wheels)|\(State.global.motor)|\(State.global.drivetrain)|\(State.global.weight)|\(State.global.program)|\(State.global.auto)|\(State.global.tele)|\(State.global.hang)|\(State.global.assist)|\(State.global.comment)
"""
     imageView.image = QRCode(text)?.image
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

