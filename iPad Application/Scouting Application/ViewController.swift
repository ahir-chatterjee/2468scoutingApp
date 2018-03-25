//
//  ViewController.swift
//  Scouting Application
//
//  Created by Vrishab Madduri on 10/30/17.
//  Copyright © 2017 Vrishab Madduri. All rights reserved.
//
import UIKit
import AsyncTimer

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    var startTime: Date? = nil
    var descriptionOptions = [""]
    var assistOptions = [""]
    var internalTimer: AsyncTimer? = nil
    var count1 = 0
    var count2 = 0
    @IBOutlet weak var matchInput: UITextField!
    @IBOutlet weak var teamInput: UITextField!
    @IBOutlet weak var matchColor: UISegmentedControl!
    @IBOutlet weak var commentInput: UITextField!
    @IBOutlet weak var autoscaleInput: UITextField!
    @IBOutlet weak var autoswitchInput: UITextField!
    @IBOutlet weak var lineControl: UISegmentedControl!
    @IBOutlet weak var penaltyControl: UISegmentedControl!
    @IBOutlet weak var AllianceSwitch: UIStepper!
    @IBOutlet weak var timerValue: UITextField!
    @IBOutlet weak var randomSwitch: UISegmentedControl!
    @IBOutlet weak var randomScale: UISegmentedControl!
    @IBOutlet weak var hangInput: UITextField!
    @IBOutlet weak var startButton: UIButton!
    @IBOutlet weak var pauseButton: UIButton!
    @IBOutlet weak var failedButton: UIButton!
    @IBOutlet weak var cancelButton: UIButton!
    
    @IBOutlet weak var successCount: UITextField!
    
    @IBOutlet weak var failedCount: UITextField!
    
    override func viewDidAppear(_ animated: Bool) {
        State.global = State()
    }
    
    @IBAction func failed(_ sender: Any) {
        State.global.failureArray[State.global.failureArray.count - 1] = true
        
        let timeElapsed = Date().timeIntervalSince(startTime!)
        
        if timeElapsed > 0.5 {
            startButton.titleLabel?.text = "Start Timer"
            State.global.timerValues.append(Int(timeElapsed))
            
            internalTimer?.stop()
            timerValue.text = ""
        }
        count2 = count2 + 1
        self.failedCount.text = String(count2)
        failedButton.isHidden = true
        failedButton.isUserInteractionEnabled = false
        cancelButton.isHidden = true
        cancelButton.isUserInteractionEnabled = false
        pauseButton.isHidden = true
        pauseButton.isUserInteractionEnabled = false
        startButton.isHidden = false
        startButton.isUserInteractionEnabled = true
        
    }
    
    
    @IBAction func start(_ sender: Any) {
        print("starting \(Date())")
        print(startButton.titleLabel)
        State.global.failureArray.append(false)
        startTime = Date()
        
        startButton.isHidden = true
        startButton.isUserInteractionEnabled = false
        
        pauseButton.isHidden = false
        pauseButton.isUserInteractionEnabled = true
        failedButton.isHidden = false
        failedButton.isUserInteractionEnabled = true
        cancelButton.isHidden = false
        cancelButton.isUserInteractionEnabled = true
        
        internalTimer = AsyncTimer(interval: .seconds(1), repeats: true, block: { () in
            self.timerValue.text = String(Int(Date().timeIntervalSince(self.startTime!)))
        })
        
        internalTimer?.start()
    }

    @IBAction func pause(_ sender: Any) {
        let timeElapsed = Date().timeIntervalSince(startTime!)
        
        if timeElapsed > 0.5 {
            startButton.titleLabel?.text = "Start Timer"
            State.global.timerValues.append(Int(timeElapsed))
            
            internalTimer?.stop()
            timerValue.text = ""
        }
           count1 = count1 + 1
        self.successCount.text = String(count1)
        pauseButton.isHidden = true
        pauseButton.isUserInteractionEnabled = false
        cancelButton.isHidden = true
        cancelButton.isUserInteractionEnabled = false
        failedButton.isHidden = true
        failedButton.isUserInteractionEnabled = false
        startButton.isHidden = false
        startButton.isUserInteractionEnabled = true
    }
    
    @IBAction func cancel(_ sender: Any) {
        internalTimer?.stop()
        timerValue.text = ""
        startButton.isHidden = false
        startButton.isUserInteractionEnabled = true
        cancelButton.isHidden = true
        cancelButton.isUserInteractionEnabled = false
        failedButton.isHidden = true
        failedButton.isUserInteractionEnabled = false
        pauseButton.isHidden = true
        pauseButton.isUserInteractionEnabled = false
        
    }
    @IBOutlet weak var OpposingSwitch: UIStepper!
    @IBOutlet weak var OpposingSwitchInput: UITextField!
    
    @IBOutlet weak var vaultInput: UITextField!
    @IBAction func vault(_ sender: UIStepper) {
        State.global.vault = Int(vaultInput.text ?? "0") ?? 0
        vaultInput.text = String(Int(sender.value) + State.global.vault)
        State.global.vault = Int(vaultInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBOutlet weak var AllianceSwitchInput: UITextField!
    
    @IBAction func autoScale(_ sender: UIStepper) {
        State.global.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        autoscaleInput.text = String(Int(sender.value) + State.global.autoscale)
        State.global.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBAction func autoSwitch(_ sender: UIStepper) {
        State.global.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        autoswitchInput.text = String(Int(sender.value) + State.global.autoswitch)
        State.global.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBAction func allianceswitchvalueChanged(_ sender: UIStepper) {
    State.global.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
    AllianceSwitchInput.text = String(Int(sender.value) + State.global.allianceswitch)
    State.global.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBOutlet weak var descriptionPicker: UIPickerView!
    
    @IBOutlet weak var assistPicker: UIPickerView!
    @IBAction func opposingallianceswitchChanged(_ sender: UIStepper) {
        State.global.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        OpposingSwitchInput.text = String(Int(sender.value) + State.global.opposingswitch)
        State.global.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        descriptionOptions = ["left", "center", "right"]
        assistOptions = ["N/A", "Failed", "Gave Assistance", "Gave Double Assist"]
        descriptionPicker.delegate = self
        descriptionPicker.dataSource = self
        assistPicker.delegate = self
        assistPicker.dataSource = self
        pauseButton.isHidden = true
        failedButton.isHidden = true
        cancelButton.isHidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
   
    @IBAction func submit(_ sender: Any) {
        State.global.color = matchColor.titleForSegment(at:  matchColor.selectedSegmentIndex) ?? "No"
        State.global.match = Int(matchInput.text ?? "0") ?? -1
        State.global.team = Int(teamInput.text ?? "0") ?? -1
        State.global.comment = String(commentInput.text!)
        State.global.penalty = penaltyControl.titleForSegment(at:  penaltyControl.selectedSegmentIndex) ?? "No"
        State.global.line = lineControl.titleForSegment(at:  lineControl.selectedSegmentIndex) ?? "No"
        State.global.hang = String(hangInput.text!)
        State.global.vault = Int(vaultInput.text ?? "0") ?? 0
        State.global.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        State.global.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        State.global.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
        State.global.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        State.global.randomSwitch = randomSwitch.titleForSegment(at:  randomSwitch.selectedSegmentIndex) ?? "No"
        State.global.randomScale = randomScale.titleForSegment(at:  randomScale.selectedSegmentIndex) ?? "No"
        let alert = UIAlertController(title: "Exiting", message: "Are you sure you want to submit?", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .`default`, handler: { _ in
            self.performSegue(withIdentifier: "SubmitSegue", sender: sender)
        }))
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("Cancel", comment: "Default action"), style: .`default`, handler: { _ in
        }))
        
        self.present(alert, animated: true, completion: nil)
    }
  
     func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if pickerView == descriptionPicker{
            return 3
        }
        else{
            return 4
        }
    }
  
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if pickerView == descriptionPicker {
            State.global.pickerView = self.pickerView(pickerView, titleForRow: row, forComponent: component)!
        } else {
            State.global.assistView = row - 1
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if(pickerView.tag == 2){
            return "\(descriptionOptions[row])"
        }else{
            return "\(assistOptions[row])"
        }
    }
}

